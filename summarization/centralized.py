from models.inference import generate_summary

def centralized_summarization(chunks, models, evaluator):
    summaries = []
    for chunk in chunks:
        summaries_per_chunk = {m: generate_summary(models[m], chunk) for m in models}
        best_summary = evaluator.evaluate_summaries(summaries_per_chunk)
        summaries.append(best_summary)
    return " ".join(summaries)