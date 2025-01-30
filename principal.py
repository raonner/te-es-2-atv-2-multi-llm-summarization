from sumarizacao.sumarizador import gerar_resumo
from avaliacao.avaliar import avaliar_resumo

# Exemplo de entrada
texto_entrada = """
Modelos de linguagem de grande escala (LLMs) transformaram o processamento de linguagem natural (PLN),
habilitando capacidades como geração de texto, sumarização e resposta a perguntas.
Diferentes modelos têm pontos fortes distintos, e combiná-los pode fornecer melhores resultados.
"""

resumo_referencia = "LLMs transformaram o PLN permitindo sumarização e geração de texto."

if __name__ == "__main__":
    for nome_modelo in ["llama", "deepseek"]:
        print(f"\nResumo gerado por {nome_modelo}:")
        resumo = gerar_resumo(texto_entrada, nome_modelo)
        print(resumo)

        print("\nAvaliação ROUGE:")
        print(avaliar_resumo(resumo_referencia, resumo))