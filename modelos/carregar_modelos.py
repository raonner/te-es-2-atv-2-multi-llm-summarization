import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from configuracoes import MODELOS

def carregar_modelo(nome_modelo):
    """
    Carrega o modelo e o tokenizador a partir do Hugging Face Model Hub.

    Args:
        nome_modelo (str): Nome do modelo conforme definido no configuracoes.py

    Returns:
        modelo (AutoModelForCausalLM): O modelo carregado
        tokenizador (AutoTokenizer): O tokenizador correspondente
    """
    tokenizador = AutoTokenizer.from_pretrained(MODELOS[nome_modelo])
    modelo = AutoModelForCausalLM.from_pretrained(
        MODELOS[nome_modelo],
        torch_dtype=torch.float16,
        device_map="auto"
    )
    return modelo, tokenizador