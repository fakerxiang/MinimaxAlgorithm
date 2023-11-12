import model

def top_k_logits(logits, k):
    if k == 0:
        # no truncation
