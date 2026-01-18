import pandas as pd
df = pd.read_csv("experiment\\datos.csv")
#print(df)
#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#Reemplazando el dato joaco por lol
df['nombre'].replace("joaco","lol",inplace=True)
print(df)

#eliminar filas con datos faltantes

df = df.dropna()

#eliminar columnas con datos faltantes

df = df.dropna(axis=1)


#print(df)

#eliminar filas repetidas
df = df.drop_duplicates()
print(df)

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("experiment\\datos.csv")
