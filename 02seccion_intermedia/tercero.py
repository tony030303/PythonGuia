#DIA 17/01. PYTHON DIA 3.
#SECCIÓN INTERMEDIA DEL CURSO(2h)

#variables 2.0

#desempaquetado
#creación de tipos de variables a través de tupla

datos = ("Lol","Sarmo",1002312)

nombre,apellido,subs = datos #tiene que ser igual a la cant. de datos en la tupla

print(nombre) 


#crear tuplas (datos de solo lectura, faster than lists)

#con tuple
tupla = tuple(["dato","otad"])

#creando una tupla sin parentésis
tupla = "dato1","dato2"
#idem, pero de un solo dato
tuplaunique = "dato1",



#Conjuntos (sets)

#con set (una tupla metida)
conjuntos = set(["dato1",("dato2","dato3")])

#conjunto dentro de otro conj

conj1 = frozenset(["dato1","dato3"])
conj2 = {conj1, "dato3"}
print(conj2)

#teoria de conjuntos
conj1 = {1,3,5,7}
conj2 = {1,3}
#es subconjunto?
resultado = conj2.issubset(conj1) #True
resultado = conj2 <= conj1 #otra forma
print(resultado)

#es superconjunto?
resultado = conj2.issuperset(conj1) #False
resultado = conj2 > conj1 #otra forma

#verificar intersección nula

resultado = conj2.isdisjoint(conj1) #False



#Diccionarios... 


#crear diccionarios con dict()

diccionario = dict(nombre="yo",apellido="Lol") #te sirve para meter diccionarios vacios al inicio

#crear diccionarios con fromkeys

diccionario = dict.fromkeys(["nombre","apellido"]) #con valores indefinidos
diccionario = dict.fromkeys(["nombre","apellido"],"algo") #con valor default "algo"



#Buclecitos


#For

# si en vez de listas pongo tuplas, funca igual.


perros = ["de raza","deanashe","lol"]

numeros = [123,22,37]

for perro,numero in zip(perros,numeros): #para recorrer más listas con mismo iterador
    print(f"recorriendo: {numero}" )
    print(f"recorriendo a {perro}")


for num in range(5,10): #5 6 7 8 9
    print(num)
    

#para recorrer con iterador (forma nooptima pq en conjuntos no funciona)

for num in range(len(numeros)):
    print(numeros[num])    
    
    
#forma correcta con indice

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(num) #aca devuelve una tupla indice,valor
    print(f'el indice es {indice} y valor es {valor}')
    
#for/else
for num in numeros:
    print(f'quepasa {num}')
else:
    print("fin o que el for no se pueda ejecutar")    




#iterar diccionarios:

diccionario = {
    'nombre': "tony",
    'apellido': "muchos"
}        

#con keys
for key in diccionario:
    print(key) #only keys
#con elementos
for datos in diccionario.items():
    print(datos) #aca devuelve tupla (key,value)
    


#uso de continue

frutas = ["banana","manchana","drogas","comidanormal"]

for fruta in frutas:
    if fruta == 'drogas':
        continue #adelanta la iteración
    print(f'{fruta}')

for fruta in frutas:
    if fruta == 'drogas':
        break #rompe el bucle
    print(f'{fruta}')

#for en una linea (para cosas rapidas obvio)

numeros = [1,2,3]

numeros_duplicados = [x*2 for x in numeros]    



#While y condiciones

contador = 0

#idem que en otros lenguajes
while contador <= 10:
    print(contador)
    contador += 1  



#funciones integradas

#build-in

#encontrar el num mayor/menor de una lista/set/tupla
lista = [1,2.23,43.2,1321.55454]

numero_mas_alto = max(lista) #1321
numero_mas_bajo = min(lista) #1
redondeando = round(numero_mas_alto,2) #y si..
print(redondeando)

#retorna false -> 0, vacio,False, None. True en caso contrario.
resultado = bool(0) #la tipica

#retorna True si todos los valores son verdaderos.

resultado = all([True,13,[],321,3,12,312]) #False si hay alguno q no cumpla
print(resultado)


resultado = sum(lista) #suma elementos

#Creando funciones (al fin pa)

def hola(num):
    x = num * 4  
    return x


ana = hola(5)
print(ana)
          
          
          
          
          
#funciones(* args)

#con operador * como parametro
def algo(algoantes, *nums):
    return sum(nums)

resultado = algo("loco",123,21312,123,1)
print(resultado)


#forzar argumentos


def hacer(dni,nombre,apellido):
    print(f'{nombre} {apellido} {dni}')


#keyword arguments    
resultado = hacer(nombre = 'yo',apellido = 'aynose',dni = 111) #otra forma de pasar parametros



#funciones lambda

dividir_pordo = lambda x: x/2 #para ahorrar abrir bloques de llamada a funciones

#filters
numeros = [12,312,3,21,321,3,123,1,312]

def es_par(num):
    if num%2==0:
        return True

numeros_pares = filter(es_par,numeros)

#en lambda

numeros_pares = filter(lambda numero: numero%2==0, numeros)
print(list(numeros_pares))           