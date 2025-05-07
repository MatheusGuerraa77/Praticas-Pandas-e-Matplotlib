import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:\DATA\Praticas-Pandas-e-Matplotlib\DATA\HaabitosDeConsumoEntreDiferentesGeracCoeesrespostas1.xlsx'

xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Sheet1")

print("Informações do DataSet")
print(df.info())
print("\n")
print("10 Primeiras Linhas")
print(df.head(10))
print("\n")
print("Colunas do DataSet")
print(df.columns)
print("\n")

print('=== lista de gerações e o número de respostas de cada uma ===')
geracoes = df['Com base no seu ano de nascimento, em qual geração você se encaixa?  '].value_counts()
print(geracoes)

plt.figure(figsize=(10, 6))
plt.bar(geracoes.index, geracoes.values)
plt.xlabel('Geração')
plt.ylabel('Número de Respostas')
plt.title('Total de Respostas por Geração')
plt.xticks(rotation=360, fontsize=5.5)

for i, valor in enumerate(geracoes.values):
    plt.text(i, valor + 1, str(valor), ha='center', fontsize=9)

plt.show()