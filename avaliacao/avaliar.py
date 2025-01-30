from evaluate import load

def avaliar_resumo(referencia, gerado):
    rouge = load("rouge")  # Agora usa o novo método correto
    pontuacoes = rouge.compute(predictions=[gerado], references=[referencia])
    return pontuacoes