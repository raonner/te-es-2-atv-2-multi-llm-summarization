from transformers import pipeline
from sumarizacao.processamento_texto import dividir_texto
from modelos.carregar_modelos import carregar_modelo


def gerar_resumo(texto, nome_modelo):
    modelo, tokenizador = carregar_modelo(nome_modelo)
    pipeline_resumo = pipeline("text-generation", model=modelo, tokenizer=tokenizador, device=0)

    trechos = dividir_texto(texto)
    resumos = [pipeline_resumo(trecho, max_length=150, do_sample=False)[0]["generated_text"] for trecho in trechos]

    return " ".join(resumos)
