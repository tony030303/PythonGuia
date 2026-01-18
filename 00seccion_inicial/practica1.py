
#inciso a
max = 7
min = 2.5
prom = 4

cursoActual = 1.5
valor = abs(min - max)
print(valor)
difRapido = 100 - (cursoActual / min * 100)
difLento = 100 - (cursoActual / max * 100)
difProm = 100 - (cursoActual / prom * 100)

print("La diferencia en porcentaje entre el curso actual y el curso...")
print(f'más rapido:  {difRapido}%')
print(f'más lento:  {difLento:.1f}%')
print(f'promedio:  {difProm}%')

#inciso b
crudoProm = 5
crudoActual = 3.5

porcReducido = 100 - cursoActual*1000 // crudoActual / 10
porcReducidoProm = 100 - prom*1000 // crudoProm / 10
print("el porcentaje reducido es...")
print(f'reducido en promedio: {porcReducidoProm}%')
print(f'reducido en el cursoactual: {porcReducido:.1f}%')


#inciso c

promedioCurso10Horas = (prom * 100 // cursoActual / 10) 

print(f'este curso con 10h equivale a {promedioCurso10Horas}hs de un curso promedio')

promedioCurso10Horas = (cursoActual * 100 // prom / 10) 

print(f'curso promedio de 10h equivale a {promedioCurso10Horas}hs de un curso actual')


print("----------------------------------------------------------------")
#ejercicio 2

palabrasPorSegundo = 2

cadena = input("ingresá una cadena con todo lo que vos digas: ")
palabrasPronunciadas = cadena.split(" ")
cantPalabras = len(palabrasPronunciadas)
segundosHablados = cantPalabras / palabrasPorSegundo 


print(f'El muchacho habló durante {segundosHablados}s y pronunció {cantPalabras} palabras.')

if segundosHablados >= 120:
    print("una banda paraaaaaaaaaaa")
    


palabrasPorSegundoDalto = 1.3 * palabrasPorSegundo
daltoHablando = cantPalabras * 10000 // palabrasPorSegundoDalto / 10000
print(f'El bldo del curso habla 30% más rapido, x ende habló durante {daltoHablando}s y pronunció {cantPalabras} palabras.')
