from sqlalchemy.orm import Session
from app.models.comment import Comment

def get_comments_for_post(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def build_comment_tree(comments):
    by_id = {c.id: {"id": c.id, "content": c.content, "user_id": c.user_id, "replies": []} for c in comments}
    roots = []
    for c in comments:
        node = by_id[c.id]
        if c.parent_id:
            parent = by_id.get(c.parent_id)
            if parent:
                parent["replies"].append(node)
        else:
            roots.append(node)
    return roots

def get_comment_depth(node):
    if not node["replies"]:
        return 1
    return 1 + max(get_comment_depth(r) for r in node["replies"])

def find_viral_chains(node, chain=None, chains=None):
    if chain is None: chain = []
    if chains is None: chains = []
    chain.append(node["id"])
    if not node["replies"]:
        chains.append(chain.copy())
    else:
        for r in node["replies"]:
            find_viral_chains(r, chain, chains)
    chain.pop()
    return chains
