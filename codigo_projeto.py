# Predição de Depressão em Estudantes
# Projeto Final - Aprendizado de Máquina - DCOMP/UFS


# 1.1 Identificação e descrição do problema
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
sns.set_theme(style="whitegrid")

URL = "https://raw.githubusercontent.com/EvilynAquino/student-depression-prediction/main/data/student_depression_dataset.csv"

df = pd.read_csv(URL)
df.head()


# 1.2 Compreensão dos dados
print(f"Registros: {df.shape[0]}")
print(f"Atributos: {df.shape[1]}")
df.info()

df.isnull().sum().sort_values(ascending=False)

print(f"Linhas duplicadas: {df.duplicated().sum()}")

df['Depression'].value_counts()

df['Depression'].value_counts(normalize=True).mul(100).round(2)

df['Sleep Duration'].value_counts()

df['Dietary Habits'].value_counts()

df['City'].value_counts().tail(25)


# 1.3 Análise exploratória
fig, ax = plt.subplots(figsize=(7,5))
sns.countplot(data=df, x='Depression', ax=ax)
ax.set_xticklabels(['Sem depressão (0)', 'Com depressão (1)'])
ax.set_title('Distribuição do atributo-alvo')
plt.show()

fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Depression', kde=True, bins=30, ax=ax)
ax.set_title('Distribuição de idade por classe de depressão')
plt.show()

fig, ax = plt.subplots(figsize=(7,5))
sns.boxplot(data=df, x='Depression', y='Academic Pressure', ax=ax)
ax.set_xticklabels(['Sem depressão', 'Com depressão'])
ax.set_title('Pressão acadêmica por classe de depressão')
plt.show()

fig, ax = plt.subplots(figsize=(7,5))
pd.crosstab(df['Have you ever had suicidal thoughts ?'], df['Depression'], normalize='index').mul(100).plot(
    kind='bar', stacked=True, ax=ax, color=['#4C72B0', '#DD8452']
)
ax.set_title('Depressão por histórico de pensamentos suicidas (%)')
ax.set_ylabel('% dentro do grupo')
ax.legend(['Sem depressão', 'Com depressão'])
plt.show()

numeric_cols = df.select_dtypes(include=[np.number]).columns.drop('id')
corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(9,7))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
ax.set_title('Matriz de correlação entre variáveis numéricas')
plt.show()

fig, ax = plt.subplots(figsize=(6,8))
df['City'].value_counts().head(15).plot(kind='barh', ax=ax)
ax.set_title('15 cidades mais frequentes no dataset')
ax.invert_yaxis()
plt.show()

print(f"Total de cidades diferentes: {df['City'].nunique()}")


# 1.5 Separação dos dados
from sklearn.model_selection import train_test_split

X = df.drop(['Depression', 'id'], axis=1)
y = df['Depression']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"Treino: {X_train.shape[0]} linhas | Teste: {X_test.shape[0]} linhas")

from sklearn.impute import SimpleImputer

colunas_numericas = X_train.select_dtypes(include=['int64', 'float64']).columns
colunas_categoricas = X_train.select_dtypes(include=['object']).columns

imputer_num = SimpleImputer(strategy='mean')
imputer_cat = SimpleImputer(strategy='most_frequent')

X_train[colunas_numericas] = imputer_num.fit_transform(X_train[colunas_numericas])
X_train[colunas_categoricas] = imputer_cat.fit_transform(X_train[colunas_categoricas])

X_test[colunas_numericas] = imputer_num.transform(X_test[colunas_numericas])
X_test[colunas_categoricas] = imputer_cat.transform(X_test[colunas_categoricas])

print("Valores ausentes tratados. Nulos restantes:", X_train.isnull().sum().sum() + X_test.isnull().sum().sum())

Q1 = X_train[colunas_numericas].quantile(0.25)
Q3 = X_train[colunas_numericas].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

mascara_treino = ~((X_train[colunas_numericas] < limite_inferior) | (X_train[colunas_numericas] > limite_superior)).any(axis=1)
print(f"Outliers removidos do treino: {(~mascara_treino).sum()} ({(~mascara_treino).sum()/len(X_train)*100:.2f}%)")

X_train = X_train[mascara_treino]
y_train = y_train[mascara_treino]

# agrupando cidades raras (e o lixo de dados tipo "Saanvi", "3.0") numa categoria só
contagem_cidades = X_train['City'].value_counts()
cidades_raras = contagem_cidades[contagem_cidades < 10].index

X_train['City'] = X_train['City'].replace(cidades_raras, 'Outras')
X_test['City'] = X_test['City'].replace(cidades_raras, 'Outras')

print(f"Cidades agrupadas em 'Outras': {len(cidades_raras)}")
print(f"Categorias de City restantes: {X_train['City'].nunique()}")

X_train = pd.get_dummies(X_train, columns=colunas_categoricas, drop_first=True)
X_test = pd.get_dummies(X_test, columns=colunas_categoricas, drop_first=True)

X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)

print("Colunas finais após encoding:", X_train.shape[1])

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_escalonado = scaler.fit_transform(X_train)
X_test_escalonado = scaler.transform(X_test)

X_train = pd.DataFrame(X_train_escalonado, columns=X_train.columns)
X_test = pd.DataFrame(X_test_escalonado, columns=X_test.columns)

print("Pré-processamento concluído. Shapes finais:", X_train.shape, X_test.shape)


# 1.6 Modelagem
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

baseline = DummyClassifier(strategy='most_frequent', random_state=42)
sgd = SGDClassifier(random_state=42, max_iter=1000)
rf = RandomForestClassifier(random_state=42, n_estimators=200)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
modelos = {'Baseline': baseline, 'SGDClassifier': sgd, 'RandomForest': rf}

resultados_cv = {}
for nome, modelo in modelos.items():
    scores = cross_val_score(modelo, X_train, y_train, cv=skf, scoring='f1')
    resultados_cv[nome] = scores
    print(f"{nome}: F1 médio (CV) = {scores.mean():.4f} (+/- {scores.std():.4f})")

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
print("Modelos treinados.")


# 1.7 Avaliação e discussão
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

modelo_final = rf
y_pred = modelo_final.predict(X_test)

print(classification_report(y_test, y_pred, target_names=['Sem depressão', 'Com depressão']))

fig, ax = plt.subplots(figsize=(6,5))
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=['Sem depressão', 'Com depressão'], ax=ax, cmap='Blues')
ax.set_title('Matriz de confusão — RandomForest (conjunto de teste)')
plt.show()

importancias = pd.Series(modelo_final.feature_importances_, index=X_train.columns).sort_values(ascending=False)
importancias.head(10).plot(kind='barh', figsize=(8,5))
plt.gca().invert_yaxis()
plt.title('Top 10 atributos mais importantes (RandomForest)')
plt.show()
