import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("experiment\\bigotes.csv")

#para hacer un gráfico d bigotes (diagramas de cajas de prob)
sns.boxplot(x="categoria",y="valor",data=df)
plt.show()