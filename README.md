# Multi-LLM Text Summarization

Este projeto implementa um framework de sumarização de textos utilizando múltiplos modelos de linguagem (LLMs), baseado no artigo *Multi-LLM Text Summarization*.

## Funcionalidades
- Divisão de textos longos em segmentos menores.
- Geração de resumos utilizando múltiplos LLMs.
- Estratégia **centralizada**: Um modelo avalia os resumos e seleciona o melhor.
- Estratégia **descentralizada**: Os modelos avaliam os resumos uns dos outros e escolhem por consenso.


## Estrutura do Projeto
```
multi-llm-summarization/
│── data/                         # Textos de entrada e resumos de referência
│── models/                       # Carregamento dos modelos LLM
│── summarization/                # Implementação das estratégias de sumarização
│── evaluation/                    # Cálculo de métricas ROUGE e BLEU
│── scripts/                       # Scripts para rodar os experimentos
│── config.py                      # Configurações globais
│── requirements.txt                # Dependências
│── README.md                      # Documentação
```

## Instalação
### Clonar o repositório e instalar dependências
```bash
git clone https://github.com/seu-usuario/multi-llm-summarization.git
cd multi-llm-summarization
pip install -r requirements.txt
```

