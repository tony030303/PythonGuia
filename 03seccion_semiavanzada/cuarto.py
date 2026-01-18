#DIA 18/01. PYTHON DIA 4.
#SECCIÓN INTERMEDIA DEL CURSO(2h)


#Modulos.

#todo archivo .py en python son módulos.

#Modulos de Python --> Creados de forma nativa en Python (escritos en C)

#Modulos de terceros --> Modulos descargados.

# Modulos propios --> Creados por nosotros

#import escondida.practica2_2 as practica2_2
#otra forma
#import practica2 as kosita #apodo para evitar nombres largos

#importar una función especifica (optimo claro)
#from escondida.practica2_2 import enlistarPrimos as enlistito,enlistarFibo 

#locko = enlistito(23) #se invoca sin ruta completa

#variable = practica2_2.esPrimo(5)
#parece que concatena lo anterior (inputs, prints)
#print(variable)

#vari = kosita.obtener_info()


#asda = escondida.practica2_2.enlistarPrimos #asi se invoca si estuviera en otro directorio

#QUE PASA SI SON DOS DIRECTORIOS DE MISMO NIVEL U DE OTROS NIVELES???

#import sys #modulo python
#print(sys.path) #importante para tener a mano la ruta 

#muy util cuando queramos importar archivos!
#sys.path.append("c:\\Users\\NoxiePC\\OneDrive\\Documentos\\proyectos tony\\facultad\\CURSOS\\PYTHON\\escondida")

#import practica2_2
#print(practica2_2.fibonacci(2))


#PAQUETES

#para que python identifique un paquete:
#__init__.py 
import paquete

#un subpaquete es aquel paquete que tiene ese identificador que a su vez es hijo de un paquete.



#ARCHIVOS .TXT
#import sys
#sys.path.append("c:\\Users\\NoxiePC\\OneDrive\\Documentos\\proyectos tony\\facultad\\CURSOS\\PYTHON\\escondida")
archivo = open("c:\\Users\\NoxiePC\\OneDrive\\Documentos\\proyectos tony\\facultad\\CURSOS\\PYTHON\\escondida\\texto.txt",encoding="UTF-8")
#print(archivo.read()) 

#leer una linea completa de un archivo (OJO CON ARCHIVOS GRANDES)
lineas = archivo.readlines()

#leer una sola linea
linea = archivo.readline() #puede incluir la cantidad de caracteres de esa linea

#cerrar archivo
archivo.close()

print(lineas)




#FORMA OPTIMA (asi nos olvidamos del close)
with open("c:\\Users\\NoxiePC\\OneDrive\\Documentos\\proyectos tony\\facultad\\CURSOS\\PYTHON\\escondida\\texto.txt",encoding="UTF-8") as archivo:
    print(archivo.read())

#solo sobreescritura 'w'    
with open("c:\\Users\\NoxiePC\\OneDrive\\Documentos\\proyectos tony\\facultad\\CURSOS\\PYTHON\\escondida\\texto.txt",'w',encoding="UTF-8") as archivo:
    #sobreescribiendo
    #archivo.write("che pero?")
    archivo.writelines(["no se que pasa","\nmisma"])   
    
    
#append 'a' para q no se pise todo
with open("c:\\Users\\NoxiePC\\OneDrive\\Documentos\\proyectos tony\\facultad\\CURSOS\\PYTHON\\escondida\\texto.txt",'a',encoding="UTF-8") as archivo:
    #sobreescribiendo
    archivo.write("\nche pero?")
    #for i in range(5):
    archivo.writelines([f'linea {i+1}\n' for i in range(5)])
    
   

#ARCHIVOS .CSV

#forma convencional
#def read_csv_in_chunks(file) para que vaya de a poco. Dsp INVESTIGAR
#import csv
#with open("experiment\\datos.csv") as archivo:
    #reader = csv.reader(archivo)
    #for i in reader:
       # print(i)   
        
        
#forma con Pandas (introducción para el data analyze)

#Entornos de JUPYTER (luego)
import pandas as pd
#Con archivos muy grandes, conviene usar
#def read_csv_in_chunks(file) para que vaya de a poco. Dsp INVESTIGAR
df = pd.read_csv("experiment\\datos.csv")
df2 = pd.read_csv("experiment\\datos.csv")
#print(df["nombre"]) #obtener los datos de la columna nombre             

#usar slicing

#ordenar el dataframe por edad
df_ordenado = df.sort_values("edad")
#print(df_ordenado)

#ordenar el df por edad (descendente)
df_ordenado = df.sort_values("edad",ascending=False)
#print(df_ordenado)

#concatenar dfs
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#acceso a las primeras i filas con head()
primer_fila = df.head(1)
#print(primer_fila)   

#acceso a las ultimas i filas con tail()
ultimas_filas = df.tail(2)
#print(ultimas_filas)

#accediendo a la cant de filas y columnas con shape

filas_columnas_totales = df.shape
filas_totales = filas_columnas_totales[0]

#ooo

filas_totales,columnas_totales = df.shape

#print(filas_totales)
#print(columnas_totales)

#stats del df (ver más adelante, parecen stats del diagrama de caja de prob)

df_info = df.describe()   

#accediendo a un elem especifico del df con loc
elem = df.loc[1,"edad"] #Segunda fila de datos, arranca en 0
#con iloc (permite que sea númerico el 2do parametro)
elem = df.iloc[1,2] #Segunda fila de datos, arranca en 0

#accediendo a todas las filas de una sola columna

apellidos = df.iloc[:,1] #aplicas el slicing!

#acceso a toda la fila 3 (idem)

fila_3 = df.loc[2,:] #idem iloc
#print(apellidos)
#print("")
#print(fila_3)

mayor_que_30 = df.loc[df["edad"] > 44,:]
print(mayor_que_30)