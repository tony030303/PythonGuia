#lista de números primos entre 0 y el num pasado

def esPrimo(num):
    divisor = 2
    flag = True
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        while flag and divisor < num:
            if num%divisor == 0: #si es divisible, no puede ser primo
                flag = False
            else:
                divisor +=1 #sino, sigo aumentando.
    return flag            

def enlistarPrimos(num):
    primos = []
    for i in range(num+1):
        if(esPrimo(i)):
            primos.append(i)
    
    return primos         

def fibonacci(num):
    if num == 1:
        return num
    elif num <= 0:
        return 0
    else:
        return fibonacci(num-1) + fibonacci(num-2)
        
        
def enlistarFibo(num):
    lista = []
    for i in range(num+1):
        lista.append(fibonacci(i))          
    return lista

numero = int(input("Calculamos primos desde cero hasta .... ? "))
primos = enlistarPrimos(numero)
print(primos)
fibo = enlistarFibo(numero)
print(fibo)            