#hallar el promedio de una lista 
def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
numeros = [5, 20, 30, 55, 80, 15]
promedio = calcular_promedio(numeros) 
print("el promedio de la lista es:", promedio) 

