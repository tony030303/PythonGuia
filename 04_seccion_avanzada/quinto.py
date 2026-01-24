#DIA 20/01. PYTHON DIA 5.
#Sección avanzada (50min)

#EVENTOS --> cosas que suceden en los programas.

#Excepciones --> eventos que joden la ejecución normal del programa

#ejemplo de excepcion simple valueError
def sumar():
    while True:
        a = input("Introduce un número: ")
        b = input("Introduce otro número: ") 
        try:
            resultado = (int(a) + int(b))

        except ValueError as e: #por ejemplo
            print("Debes introducir números válidos")
            print(e)
        except ZeroDivisionError as ex:
            print(ex)    
        else:
            break
        finally:
            print("Siempre me voy a ejecutar pa")
    
    return resultado

#print(sumar())



#Excepciones regulares (para encontrar coincidencias en patrones)
import re

texto = '''hola mundo, hoy es 20/01/20242312312 .
y mañana será 21/01/2024 abasbdabdbasbaababab.
sanias esa?.
hola'''

resultado = re.search("hola",texto) #devuelve la primera coincidencia
resultado = re.findall("hoy",texto) #devuelve todas las coincidencias

#\d --> busca digitos númericos
resultado = re.findall(r"\d",texto) #devuelve todas las coincidencias numericas.

#\D --> busca todo menos digitos númericos
resultado = re.findall(r"\D",texto)

#\w --> busca caracteres de palabras (letras, números, guion bajo)
resultado = re.findall(r"\w",texto)

# \W --> busca todo menos caracteres de palabras
resultado = re.findall(r"\W",texto)

# \n --> busca saltos de línea
resultado = re.findall(r"\n",texto)

# \s --> busca espacios en blanco (espacios, tabulaciones, saltos de línea)
resultado = re.findall(r"\s",texto)

# \S --> busca todo menos espacios en blanco
resultado = re.findall(r"\S",texto)

# . -> busca cualquier caracter excepto saltos de línea
resultado = re.findall(r".",texto)

# \ --> cancelar caracteres especiales (todos q no son alfanumericos)

resultado = re.findall(r'\.',texto)

# armando una cadena ue busque num-punto-espacio in that order

resultado = re.findall(r'\d\.\s', '1. hola mundo 2. adios mundo 3.hola de nuevo')

#encontrar algo al principio de una linea:
resultado = re.findall(r'^hola', texto)

#aca cada linea la interpreta como el comienzo de una linea dentro del multilinea string
resultado = re.findall(r'^hola', texto, re.MULTILINE)


#final de una linea:
#con lo de multilinea es idem que lo de arriba
resultado = re.findall(r'será.$', texto, re.MULTILINE)

#Grupos: Busca n cantidad de veces el valor de la izq
resultado = re.findall(r'\d{2}/\d{2}/\d{4}', texto) #busca fechas en formato dd/mm/aaaa

#rangos: Busca n cantidad de veces (con max de m veces)
resultado = re.findall(r'\d{2,4}', texto) #busca numeros de 2 a 4 digitos
#de un mismo numero, lo puede dividir varias veces...

#buscar solo ab
resultado = re.findall(r'(ab){2,4}', texto)


# | --> busca una cosa o la otra (si se cumplen las dos, retorna ambas)

resultado = re.findall(r'hola|\d{2,4}', texto)
print(resultado)



#Ejemplo:
text = "La fecha es 25/12/2023 y hay otra 24/01/2001 y la hora es 14:30."

pattern = r'(\d{2}/\d{2}/\d{4})'

replacement = "****"

new_text = re.sub(pattern, replacement, text)

resultado = new_text
print(resultado)



#ejemplo2

email = "sarmanotni@gmail.com"

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#el + significa al menos una vez
#el % significa "una o mas veces"
result = re.match(pattern,email) #devuelve true si hay coincidencia

if result:
    print("bien ahi, es")
else: 
    print("no.")

