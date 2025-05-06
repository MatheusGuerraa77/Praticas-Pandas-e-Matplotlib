"""
✅ Questão 1: Preferência entre lojas físicas e online A equipe de marketing deseja entender a preferência dos consumidores entre comprar em lojas físicas ou online, a fim de direcionar melhor as estratégias de venda.

📌 Tarefa:

Calcule o total de respostas para cada preferência de compra (loja física, loja online, ambas, etc.).

Crie um gráfico de rosca (ou pizza) representando a proporção de cada categoria.

Interprete visualmente qual modelo de loja é mais valorizado pelos participantes.

🎯 Dica:

A coluna usada será: ➤ "Entre compras em lojas online e lojas físicas, qual é mais importante para você?"

"""

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

print('=== total de respostas para cada preferência de compra (loja física, loja online, ambas, etc.)===')
preferencia_compra = df['Entre compras em lojas online e lojas físicas, qual é mais importante para você?'].value_counts()
print(preferencia_compra)

plt.figure(figsize=(8, 8))
plt.pie(preferencia_compra, labels=preferencia_compra.index, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 1.0})
plt.title('Preferência de Compra entre Lojas Físicas e Online')
plt.legend(title='Preferência', loc='upper left')
plt.axis('equal')
plt.show()