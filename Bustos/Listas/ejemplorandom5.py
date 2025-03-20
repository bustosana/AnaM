#hallar la mediana de una lista
def encontrar_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada) 
    
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        return (medio1 + medio2) / 2

numeros = [2, 12, 8, 9, 25]
print("La mediana es:", encontrar_mediana(numeros))

#crear paquetes en python
import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def medianaLista(lista):          
    mediana = lista[0]
    sum=0
    # for i in range(len(lista)):
    #     sum+=lista[i]

vector=[]
tam=random.randint(5,20)
vector=llenarListaRandom(vector,tam)
print(vector)
print(medianaLista(vector))