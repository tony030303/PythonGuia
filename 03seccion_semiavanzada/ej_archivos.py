#dos listas (una con nombres, otra con apellidos) llevadas a un .txt


nombres = ["Lucas","Marcelo","Roberto"]
apellidos = ["Sanchez","Veira","Carlos"]



with open("experiment\\info.txt",'a',encoding="UTF-8") as archivo:
    #for nombre,apellido in zip(nombres,apellidos):
        #archivo.writelines([f'{nombre} {apellido}\n'])
    
    #for de una linea 
    [archivo.writelines(f'Nombre: {nombre} Apellido: {apellido}\n' for nombre,apellido in zip(nombres,apellidos))] 