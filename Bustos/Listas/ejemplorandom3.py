#sumar los elementos de una lista que ya este llena
def sumar_elementos(lista):
    suma = sum(lista)
    return suma

numeros = [8, 15, 25, 75, 80]
resultado = sumar_elementos(numeros)
print("La suma de los elementos es:", resultado)

#crear paquetes en python
import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def sumLista(lista):          
    sum = lista[0]
    sum=0
    # for i in range(len(lista)):
    #     sum+=lista[i]
    for x in lista:
        if x > sum:
            sum = x
    return f"la suma es:{sum}"

vector=[]
tam=random.randint(5,20)
vector=llenarListaRandom(vector,tam)
print(vector)
print(sumLista(vector))