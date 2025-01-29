from models.inference import generate_summary

def decentralized_summarization(chunks, models):
    summaries = []
    for chunk in chunks:
        summaries_per_chunk = {m: generate_summary(models[m], chunk) for m in models}
        votes = {m: sum(1 for v in summaries_per_chunk.values() if v == summaries_per_chunk[m]) for m in summaries_per_chunk}
        best_summary = max(votes, key=votes.get)
        summaries.append(summaries_per_chunk[best_summary])
    return " ".join(summaries)