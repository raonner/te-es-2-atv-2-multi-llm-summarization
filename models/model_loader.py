from transformers import AutoModelForCausalLM, AutoTokenizer
from config import MODEL_NAMES

def load_models():
    tokenizers = {m: AutoTokenizer.from_pretrained(m) for m in MODEL_NAMES}
    models = {m: AutoModelForCausalLM.from_pretrained(m) for m in MODEL_NAMES}
    return tokenizers, models