from collections import Counter, defaultdict
import re
from threading import Lock
from typing import List, Tuple, Dict, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text

HASHTAG_RE = re.compile(r"#([A-Za-z0-9_]+)")

class HashtagEngine:
    def __init__(self):
        self._counter = Counter() 
        self._post_map = defaultdict(set) 
        self._lock = Lock()
    @staticmethod
    def extract_tags(text: str) -> List[str]:
        if not text:
            return []
        return [m.group(1).lower() for m in HASHTAG_RE.finditer(text)]
    
    def ingest_post(self, post_id: int, tags: List[str], db: Optional[Session] = None) -> None:

        tags = list(dict.fromkeys([t.lower() for t in tags]))  # unique preserve order
        if not tags:
            return

        with self._lock:
            existing = self._post_map.get(post_id, set())
            to_add = set(tags) - existing
            if not to_add:
                return
            for t in to_add:
                self._counter[t] += 1
            self._post_map[post_id].update(to_add)

        if db is not None:
            self._persist_tags_to_db(post_id, list(to_add), db)

    def get_trending(self, limit: int = 10) -> List[Tuple[str, int]]:
        return self._counter.most_common(limit)

    def _persist_tags_to_db(self, post_id: int, tags: List[str], db: Session) -> None:
        if not tags:
            return
        placeholders = ", ".join([f"(:tag{i})" for i in range(len(tags))])
        params = {f"tag{i}": tags[i] for i in range(len(tags))}

        # Insert tags if not exists
        upsert_sql = text(
            f"""
            INSERT INTO hashtags (tag, count)
            SELECT t.tag, 0 FROM (VALUES {', '.join([f"(:tag{i})" for i in range(len(tags))])}) AS t(tag)
            WHERE NOT EXISTS (SELECT 1 FROM hashtags h WHERE h.tag = t.tag)
            """
        )
        db.execute(upsert_sql, params)
        fetch_sql = text(
            "SELECT id, tag FROM hashtags WHERE tag = ANY(:tags)"
        )
        rows = db.execute(fetch_sql, {"tags": tags}).mappings().all()
        tag_to_id = {r["tag"]: r["id"] for r in rows}
        for tag in tags:
            hashtag_id = tag_to_id.get(tag)
            if not hashtag_id:
                continue
            insert_link_sql = text(
                """
                INSERT INTO post_hashtags (post_id, hashtag_id)
                SELECT :post_id, :hashtag_id
                WHERE NOT EXISTS (
                    SELECT 1 FROM post_hashtags ph WHERE ph.post_id = :post_id AND ph.hashtag_id = :hashtag_id
                )
                """
            )
            res = db.execute(insert_link_sql, {"post_id": post_id, "hashtag_id": hashtag_id})
            update_count_sql = text(
                """
                UPDATE hashtags
                SET count = count + 1
                WHERE id = :hashtag_id
                AND EXISTS (
                    SELECT 1 FROM post_hashtags ph WHERE ph.post_id = :post_id AND ph.hashtag_id = :hashtag_id
                )
                """
            )
            db.execute(update_count_sql, {"hashtag_id": hashtag_id, "post_id": post_id})
    def recommend(self, tag: str, db: Session, min_cooccurrence: float = 0.3, top_n: int = 3) -> List[Tuple[str, int, float]]:
        tag = tag.lower()
        tag_row = db.execute(text("SELECT id, count FROM hashtags WHERE tag = :tag"), {"tag": tag}).mappings().first()
        if not tag_row:
            return []

        tag_id = tag_row["id"]

        sql = text(
            """
            SELECT h2.tag AS tag, COUNT(*) AS co_count
            FROM post_hashtags ph1
            JOIN post_hashtags ph2 ON ph1.post_id = ph2.post_id
            JOIN hashtags h2 ON ph2.hashtag_id = h2.id
            WHERE ph1.hashtag_id = :tag_id AND ph2.hashtag_id != :tag_id
            GROUP BY h2.tag
            ORDER BY co_count DESC
            LIMIT :limit
            """
        )

        rows = db.execute(sql, {"tag_id": tag_id, "limit": 100}).mappings().all()
        denom_row = db.execute(text("SELECT COUNT(*) AS c FROM post_hashtags WHERE hashtag_id = :tag_id"), {"tag_id": tag_id}).mappings().first()
        denom = denom_row["c"] if denom_row else 0
        if denom == 0:
            return []

        results = []
        for r in rows:
            co = r["co_count"]
            ratio = co / denom
            if ratio >= min_cooccurrence:
                results.append((r["tag"], co, ratio))
            if len(results) >= top_n:
                break

        return results
