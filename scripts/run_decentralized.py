from models.model_loader import load_models
from summarization.chunking import chunk_text
from summarization.decentralized import decentralized_summarization
from evaluation.rouge_eval import compute_rouge
from evaluation.bleu_eval import compute_bleu

if __name__ == "__main__":
    text = open("data/input_texts/sample.txt").read()
    reference_summary = open("data/reference_summaries/sample_summary.txt").read()

    tokenizers, models = load_models()
    chunks = chunk_text(text)

    summary = decentralized_summarization(chunks, models)

    print("ROUGE:", compute_rouge(summary, reference_summary))
    print("BLEU:", compute_bleu(summary, reference_summary))