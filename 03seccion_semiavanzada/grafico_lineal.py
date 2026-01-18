import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("experiment\\pulsaciones.csv")

#para hacer un gráfico lineal con los datos que mandamos
sns.lineplot(x="fecha",y="pulsaciones",data=df)
plt.plot("01-04",55,"o") #para hacer un punto en el pico hardcodeado.
plt.show() #mostrarlo


#Gráfico de barras