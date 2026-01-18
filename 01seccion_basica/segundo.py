#DIA 16/01. PYTHON DIA 2.
#SECCIÓN BÁSICA DEL CURSO(1H)

#String Methods

cadena = "hOlaqueacaeasdase"
variable = dir(cadena) #importante (te da la lista de métodos que podes usar con cada tipo de dato)

#los métodos son propios de los tipos de datos, no son funciones..

print(cadena.upper()) #A mayus
print(cadena.lower()) #A minus
print(cadena.capitalize()) #Primera mayus
print(cadena.casefold()) #a minus (más poder q lower)
print(cadena.find("z")) #devuelve la pos del 1er valor donde salga eso (-1 sino)
print(cadena.index("a")) #idem q arriba, pero excepción sino
print(cadena.isnumeric()) #devuelve false porque no es num
print(cadena.isalpha()) # true (xq es cadena alfanúmerica)
#el espacio no es alfanumerico, ahi devolveria false
print(cadena.count("a")) # devuelve 5 aes
print(len(cadena)) #longitud
print(cadena.endswith("e")) #true
print(cadena.startswith("z")) #False
print(cadena.replace("a","x")) #a --> x en la cadena
print(cadena.split("a")) #ignora la a igual, hace la lista d palabras desde cadena


#List methods

lista = ["Juan", 232, "Perú", 1.72]

print(dir(lista))

#aca tambien existe el index y el count para encontrar la pos de un elemento o la cant de datos repetidos

print(len(lista)) #retorna 4
lista.append("vomitodecabra") #mete elementos al final de la lista
print(lista)
lista.insert(0, "ke") #en la pos donde querramos.
print(lista)
lista.extend(["a",2]) #funciona como unión de listas
print(lista)

lista.pop(0) #elimina elem en pos
print(lista)

lista.remove("vomitodecabra") #elimina elem con su dato
print(lista)

lista.clear() #elimina todo
print(lista)
lista.extend(["aadsa","bbbb","aasad","cccc","balon"])
lista.sort(reverse=False) #ordena en orden ascendente
print(lista)
lista.sort(reverse=True) #ordena en orden descendente
print(lista)
lista.sort(key=len,reverse=False) #por longitud d menor a mayor
print(lista)

lista.reverse() #revertirnomas
print(lista)


#Dictionary Methods

diccionario = {
    'nombre': "Yo padre",
    23: 22,
    'peso': 160.3
}

print(dir(diccionario))
#aca tmb  funciona el clear..

print(diccionario.keys()) #las claves del diccionario
print(diccionario.get("""nombre""")) # retorna el elem que apunta la clave (sinexcepción)
print(diccionario.pop(23)) #borra a partir de clave 
print(diccionario.items()) #items de un diccionario



#Input interacción

edad = input("asi es como se piden datos ahora... ")

print(f'a ver: {edad} ')