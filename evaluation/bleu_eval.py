from nltk.translate.bleu_score import sentence_bleu

def compute_bleu(generated, reference):
    return sentence_bleu([reference.split()], generated.split())