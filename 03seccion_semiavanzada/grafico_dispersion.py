import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("experiment\\dispersion.csv")

#para hacer un gráfico d dispersión (los puntitos en el aire)
sns.scatterplot(x="tiempo",y="dinero",data=df)
plt.show()

