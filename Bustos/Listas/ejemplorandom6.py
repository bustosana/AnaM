#hallar la varianza de una lista 
def calcular_varianza(lista):
    n = len(lista)  
    if n == 0:
        return None
    
    media = sum(lista) / n 
    suma_diferencias = sum((x - media) ** 2 for x in lista)  
    varianza = suma_diferencias / n  
    
    return varianza

numeros = [8, 4, 55, 15, 10]
print("La varianza es:", calcular_varianza(numeros))

#crear paquetes en python
import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def varianzaLista(lista):          
    varianza = lista[0]
    sum=0
    # for i in range(len(lista)):
    #     sum+=lista[i]

vector=[]
tam=random.randint(5,20)
vector=llenarListaRandom(vector,tam)
print(vector)
print(varianzaLista(vector))