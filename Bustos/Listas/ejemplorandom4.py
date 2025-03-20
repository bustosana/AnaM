#hallar el promedio de una lista 
def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
numeros = [5, 20, 30, 55, 80, 15]
promedio = calcular_promedio(numeros) 
print("el promedio de la lista es:", promedio) 

import random
def llenarlistarandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
        return lista
    def promediolista(lista):
        
        promedio = 0
        #for i in range(len(lista)):
        #  sum+lista[1]

    vector={}
    tam=random.randint(5,20)
    vector=llenarlistarandom(vector,tam)
    print(vector)
    print(promediolista(vector))
