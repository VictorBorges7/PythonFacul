import seaborn as sns
import matplotlib.pyplot as plt

# Estilo do gráfico
sns.set(style="whitegrid")

# Dataset exemplo
df = sns.load_dataset('tips')

# 1º gráfico: Total de gastos por período
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette="Set2")
plt.xlabel('Período (Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de Gastos por Período (Almoço ou Jantar)')
plt.show()

# 2º gráfico: Média de gastos por período
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, palette="Set2")  # padrão = média
plt.xlabel('Período (Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de Gastos por Período (Almoço ou Jantar)')
plt.show()

# 3º gráfico: Média da gorjeta por período
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='tip', data=df, palette="Set3")
plt.xlabel('Período (Time)')
plt.ylabel('Média da Gorjeta')
plt.title('Média da Gorjeta por Período (Almoço ou Jantar)')
plt.show()
