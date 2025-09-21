from collections import defaultdict
hashtag_counts = defaultdict(int)
co_occurrence = defaultdict(lambda: defaultdict(int))

def add_hashtags(post_hashtags: list[str]):
    for i, tag in enumerate(post_hashtags):
        hashtag_counts[tag] += 1
        for j, other in enumerate(post_hashtags):
            if i != j:
                co_occurrence[tag][other] += 1

def get_trending(limit=5):
    return sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)[:limit]

def recommend(tag: str):
    if tag not in co_occurrence:
        return []
    total = hashtag_counts[tag]
    related = [(other, count) for other, count in co_occurrence[tag].items() if count / total > 0.3]
    related.sort(key=lambda x: x[1], reverse=True)
    return [t for t, _ in related[:3]]
