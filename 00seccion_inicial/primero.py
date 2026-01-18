#DIA 15/01. PYTHON DIA 1.
#NADA MUY RELEVANTE, COSAS YA APRENDIDAS. 
# LOS DICCIONARIOS, CONJ Y EL MANEJO DE LISTAS PUEDE SER INTERESANTE.

#DATOS SIMPLES, VARIABLES

"""asdsada
asdas quie paso """ #formas de poner texto en varias lineas

ola = '''\nasadasd
que paso'''

bo = True and True

como = 55
negrito = "porque vamos acá?"

ke = f"\n{como}" + negrito  # con f haces el casteo
del como #borrar variables (liberas espacio)
del negrito
print(ke)

print("55" in ke) #operador de inclusión, en texto
print("gorila" not in ke) #operador de inclusión, en texto

#DATOS COMPUESTOS.

l = ["quepa", 69, 32.1, True, "quepaso"] #listas mutables
tupla = ("quepaso", 58) #datos inmutables (tuplas)
l[0] = "arraybound"

print(l)
print(l[2]) #la tipicaaa
#conjuntos (datos intercambiables), similar listas, no se repiten valores
#no hay indices (se accede por bucles, otra forma)

conj = {"quepa", 69, 32.1, True, "quepaso", 23232}
print("quepa" in conj) #este operador tmb sirve para encontrar elementos en conjunto.
print(conj)

#diccionario (formato similar a los JSON) (key : value)

diccionario = {
    'nombre': "Yo padre",
    'edad': 22,
    'peso': 160.3
}

print(diccionario['nombre']) #acceso a datos a través de indices creados.



#OPERADORES ARITMETICOS

a = 20
b = 15

c = []

c.append(a+b) #agregar elemento a la lista.
c.append(a-b)
c.append(a*b)
c.append(a/b)
c.append(a%b)
c.append(a**b) #exponente potencia
b = 16.5
b = str(b)
print(type(b)) #para saber los tipos de los datos.

#c.append(int(a//b)) #división entera. Casteo de Float --> Int
print(c)

#OPERADORES DE COMPARACIÓN
5 == 6
5 != 6
5 > 6 # >= , <= , <
24324214 

del a
del b

a = 5
b = 20
z = 60

comp = (a-b) >= z #combinando operadorres

print(comp)


#CONDICIONALES

edad = 45

if edad == 18:
    print("tenes 18")
else:
    if edad > 18:
        print("sos un viejardoo")
    else:
        print("nenaazoooo")
        
        
        
matricula = 1240

if matricula > 1000:
    print("genio del futbol mundial")
elif matricula > 500: #else if = elif (python)
    print("podia pasar... siga siga")

else:
    print("flojito che")            
          
        
#OPERADORES LÓGICOS 
#se puede usar and / &. 
# or / |
# not False ...  not True
#repaso.

resultado = True & True | False and not False
print(resultado)