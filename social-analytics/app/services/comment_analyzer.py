from sqlalchemy.orm import Session
from app.models.comment import Comment
from functools import lru_cache

class CommentAnalyzer:
    def __init__(self):
        pass

    def get_comment_tree(self, post_id: int, db: Session):
        roots = (
            db.query(Comment)
            .filter(Comment.post_id == post_id, Comment.parent_id == None)
            .all()
        )

        def build_tree(comment):
            children = (
                db.query(Comment).filter(Comment.parent_id == comment.id).all()
            )
            return {
                "id": comment.id,
                "user_id": comment.user_id,
                "content": comment.content,
                "created_at": comment.created_at,
                "replies": [build_tree(child) for child in children],
            }

        return [build_tree(c) for c in roots]
    def calculate_engagement_depth(self, comment_tree):
        def depth(node):
            if not node["replies"]:
                return 1
            return 1 + max(depth(child) for child in node["replies"])

        return max((depth(c) for c in comment_tree), default=0)
    def count_total_replies(self, comment_tree):
        def count(node):
            return len(node["replies"]) + sum(count(child) for child in node["replies"])

        return sum(count(c) for c in comment_tree)

    def find_viral_chains(self, comment_tree, min_length=3):
        viral_chains = []

        def dfs(node, path):
            new_path = path + [node["id"]]

            if len(new_path) >= min_length:
                viral_chains.append(new_path)

            for child in node["replies"]:
                dfs(child, new_path)

        for root in comment_tree:
            dfs(root, [])

        return viral_chains
    
    @lru_cache(maxsize=128)
    def engagement_score(self, post_id: int, db: Session):
        tree = self.get_comment_tree(post_id, db)
        depth = self.calculate_engagement_depth(tree)
        replies = self.count_total_replies(tree)

        return {"depth": depth, "total_replies": replies, "score": depth * replies}
