# Predição de Depressão em Estudantes

Projeto Final — Aprendizado de Máquina — DCOMP/UFS

## Objetivo

Prever se um estudante apresenta indícios de depressão a partir de características demográficas, acadêmicas e de estilo de vida, contribuindo para a identificação precoce de casos de risco.

## Integrantes

| Nome | GitHub | Parte |
|---|---|---|
| Mateus | @Mat-Macedo | Dados e Análise Exploratória |
| Luan | @luanorama | Pré-processamento e Separação dos dados |
| Evilyn | @EvilynAquino | Modelagem e Avaliação |

## Fonte dos dados

[Student Depression Dataset — Kaggle](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)

O dataset está disponível em `data/student_depression_dataset.csv` neste repositório e é carregado diretamente pelo notebook via URL raw do GitHub (não depende de arquivos locais).

## Tipo da tarefa

**Classificação binária** — o atributo-alvo `Depression` indica se o estudante apresenta (1) ou não (0) indícios de depressão.

## Organização dos arquivos

```
.
├── README.md
├── notebook.ipynb
├── projeto_completo.py       (versão em script único do pipeline, para execução fora do notebook)
└── data/
    └── student_depression_dataset.csv
```

## Como abrir o notebook no Google Colab

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. Vá em `Arquivo > Abrir notebook > GitHub`
3. Cole a URL deste repositório e selecione `notebook.ipynb`

Ou clique direto no botão (atualizar o link após subir o repo):

`https://colab.research.google.com/github/EvilynAquino/student-depression-prediction/blob/main/notebook.ipynb`

## Modelos utilizados

- Baseline (DummyClassifier) — F1 (validação cruzada): 0,7388
- SGDClassifier — F1 (validação cruzada): 0,8587
- RandomForestClassifier — F1 (validação cruzada): 0,8693 — **modelo escolhido como final**

## Principais resultados

O **RandomForestClassifier** foi o modelo com melhor desempenho, tanto na validação cruzada (5 folds) quanto no conjunto de teste reservado:

- **Acurácia:** 84,0%
- **Precisão (classe "com depressão"):** 84,9%
- **Revocação (classe "com depressão"):** 88,3%
- **F1-score:** 86,6%

O atributo mais relevante para o modelo foi `Have you ever had suicidal thoughts?` (histórico de pensamentos suicidas), seguido por `Academic Pressure` (pressão acadêmica) e `Financial Stress` (estresse financeiro). Essa relação já havia sido identificada na análise exploratória e é discutida criticamente na seção 1.7 do notebook, incluindo uma reflexão ética sobre o uso desse atributo como preditor.

## Divisão das contribuições

| Integrante | Contribuição |
|---|---|
| Mateus (@Mat-Macedo) | Seções 1.1, 1.2, 1.3 (dados e análise exploratória) |
| Luan (@luanorama) | Seções 1.4, 1.5 (pré-processamento e separação dos dados) |
| Evilyn (@EvilynAquino) | Seções 1.6, 1.7 (modelagem e avaliação) |

## Link do vídeo

(https://youtu.be/zD8zPC_laDg?si=1rgoRmP-6iOKPRVC)

## Declaração de uso de ferramentas de inteligência artificial

- **Ferramenta utilizada:** Claude (Anthropic)
- **Finalidade:** apoio na organização do repositório GitHub, na revisão de código (incluindo identificação de um problema de vazamento de dados no pré-processamento) e no esclarecimento de dúvidas técnicas ao longo do desenvolvimento
- **Parte do trabalho em que foi utilizada:** estruturação inicial do repositório e do notebook; revisão do pré-processamento (seções 1.4 e 1.5); apoio na etapa de modelagem e avaliação (seções 1.6 e 1.7)
- **Forma de verificação:** todo código foi executado do início ao fim antes de ser incorporado ao notebook final, e os resultados (métricas, gráficos) foram conferidos pelos integrantes responsáveis por cada seção
