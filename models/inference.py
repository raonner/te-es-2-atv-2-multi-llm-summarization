import torch

def generate_summary(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        output = model.generate(**inputs, max_length=160, do_sample=True)
    return tokenizer.decode(output[0], skip_special_tokens=True)