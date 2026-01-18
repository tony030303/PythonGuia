import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("experiment\\cofla_ingresos.csv")

#para hacer un gráfico d barras
sns.barplot(x="fuente",y="ingresos",data=df)

#mostrando el total
total_ingresos = df['ingresos'].sum()
print(f'el total es ${total_ingresos} USD')
plt.show()