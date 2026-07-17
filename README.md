# Predição de Depressão em Estudantes

Projeto Final — Aprendizado de Máquina — DCOMP/UFS

## Objetivo

Prever se um estudante apresenta indícios de depressão a partir de características demográficas, acadêmicas e de estilo de vida, contribuindo para a identificação precoce de casos de risco.

## Integrantes

| Nome | GitHub | Parte |
|---|---|---|
| — | @EvilynAquino | Dados e Análise Exploratória |
| — | @Mat-Macedo | Pré-processamento e Separação dos dados |
| — | @luanorama | Modelagem e Avaliação |

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
└── data/
    └── student_depression_dataset.csv
```

## Como abrir o notebook no Google Colab

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. Vá em `Arquivo > Abrir notebook > GitHub`
3. Cole a URL deste repositório e selecione `notebook.ipynb`

Ou clique direto no botão (atualizar o link após subir o repo):

`https://colab.research.google.com/github/SEU_USUARIO/SEU_REPOSITORIO/blob/main/notebook.ipynb`

## Modelos utilizados

- Baseline (DummyClassifier)
- SGDClassifier
- RandomForestClassifier

*(atualizar após a modelagem estar concluída)*

## Principais resultados

*(preencher após a avaliação dos modelos: melhor modelo, métricas alcançadas, etc.)*

## Divisão das contribuições

| Integrante | Contribuição |
|---|---|
| @EvilynAquino | Seções 5.1, 5.2, 5.3 (dados e análise exploratória) |
| @Mat-Macedo | Seções 5.4, 5.5 (pré-processamento e separação dos dados) |
| @luanorama | Seções 5.6, 5.7 (modelagem e avaliação) |

## Link do vídeo

*(inserir link do vídeo aqui)*

## Declaração de uso de ferramentas de inteligência artificial

*(preencher conforme o uso real, por exemplo:)*

- **Ferramenta utilizada:** Claude (Anthropic)
- **Finalidade:** apoio na estruturação do notebook, revisão de código e organização do projeto
- **Parte do trabalho em que foi utilizada:** *(especificar)*
- **Forma de verificação:** todo código gerado foi executado e revisado pelos integrantes antes de ser incorporado ao notebook final
