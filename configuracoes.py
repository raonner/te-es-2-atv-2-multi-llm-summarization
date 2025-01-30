# configuracoes.py

MODELOS = {
    "llama": "meta-llama/Llama-2-7b-chat-hf",
    "deepseek": "deepseek-ai/deepseek-llm-7b"
}

TAMANHO_MAX_CHUNK = 512  # Tamanho máximo do chunk para dividir os textos longos
TAMANHO_MAX_RESUMO = 150  # Número máximo de tokens no resumo