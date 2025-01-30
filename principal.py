import os
from sumarizacao.sumarizador import gerar_resumo
from avaliacao.avaliar import avaliar_resumo

# Caminhos das pastas
PASTA_ENTRADA = "dados/textos_entrada/"
PASTA_RESUMOS = "dados/resumos/"
PASTA_AVALIACAO = "dados/avaliacoes/"

# Criar pastas se ainda não existirem
os.makedirs(PASTA_RESUMOS, exist_ok=True)
os.makedirs(PASTA_AVALIACAO, exist_ok=True)

# Iterar sobre todos os arquivos de entrada
for arquivo in os.listdir(PASTA_ENTRADA):
    caminho_arquivo = os.path.join(PASTA_ENTRADA, arquivo)

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    print(f"\n🔹 Gerando resumo para: {arquivo}")

    # Definir um resumo de referência manual (pode ser modificado depois)
    resumo_referencia = "Texto resumido esperado para esse documento."

    # Criar dicionário para salvar as avaliações
    resultados_avaliacao = {}

    # Gerar resumos com os modelos disponíveis
    for modelo in ["llama", "deepseek"]:
        resumo = gerar_resumo(texto, modelo)

        # Criar nome do arquivo de saída
        caminho_resumo = os.path.join(PASTA_RESUMOS, f"{modelo}_{arquivo}")

        # Salvar o resumo gerado
        with open(caminho_resumo, "w", encoding="utf-8") as f:
            f.write(resumo)

        print(f"Resumo salvo em {caminho_resumo}")

        # Avaliar o resumo gerado
        print(f"📊 Avaliando resumo gerado por {modelo}...")
        avaliacao = avaliar_resumo(resumo_referencia, resumo)
        resultados_avaliacao[modelo] = avaliacao

    # Salvar a avaliação no arquivo correspondente
    caminho_avaliacao = os.path.join(PASTA_AVALIACAO, f"avaliacao_{arquivo.replace('.txt', '.json')}")
    with open(caminho_avaliacao, "w", encoding="utf-8") as f:
        f.write(str(resultados_avaliacao))  # Salvamos como string JSON

    print(f"Avaliação salva em {caminho_avaliacao}")