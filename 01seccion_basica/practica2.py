#alumno con menor edad --> asistente
#alumno con mayor edad --> profesor

def obtener_info(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("ingrese nombre del alumno: ")
        edad = int(input("ingrese la edad del alumno: "))
        compañero = (nombre,edad) #tupla
        compañeros.append(compañero)
    
    compañeros.sort(key=lambda x: x[1]) #ordenar por edad
    asistente = compañeros[0][0]
    profesor = compañeros[cantidad-1][0]
    return compañeros, asistente, profesor

cantidad = int(input("cuantos alumnos vinieron? "))
if(cantidad > 1):
    compañeros,asistente,profesor = obtener_info(cantidad)
    for nombre,edad in compañeros:
        print(f'{nombre}, {edad} años. ')
    print(f'\nProfe? {profesor}')
    print(f'Asistente? {asistente}')
        
else:
    print("pelotudeces acá no. Intentá de nuevo.")
        