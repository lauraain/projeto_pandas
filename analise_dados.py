import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. Ler arquivo CSV
# ----------------------------
df = pd.read_csv('exemplo_dados.csv')

print("Dados do CSV:")
print(df)

# ----------------------------
# 2. Estatísticas básicas
# ----------------------------
print("\nEstatísticas descritivas:")
print(df.describe())

# ----------------------------
# 3. Gráfico de barras (Salário por Nome)
# ----------------------------
sns.barplot(x='Nome', y='Salario', data=df)
plt.title("Salário por Nome")
plt.show()

