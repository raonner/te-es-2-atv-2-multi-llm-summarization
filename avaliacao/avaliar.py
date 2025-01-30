from datasets import load_metric

def avaliar_resumo(referencia, gerado):
    rouge = load_metric("rouge")
    pontuacoes = rouge.compute(predictions=[gerado], references=[referencia])
    return pontuacoes