def get_comment_depth(comment: dict):
    if not comment.get("replies"):
        return 1
    return 1 + max(get_comment_depth(reply) for reply in comment["replies"])

def find_viral_chains(comment: dict, chain=None, chains=None):
    if chain is None: chain = []
    if chains is None: chains = []
    chain.append(comment["id"])
    if not comment.get("replies"):
        chains.append(chain.copy())
    else:
        for reply in comment["replies"]:
            find_viral_chains(reply, chain, chains)
    chain.pop()
    return chains
