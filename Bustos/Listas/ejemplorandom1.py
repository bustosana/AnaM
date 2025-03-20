#crear paquetes en python
import random
def llenarListaRandom(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista

def menorLista(lista):          
    menor = lista[0]
    sum=0
    # for i in range(len(lista)):
    #     sum+=lista[i]
    for x in lista:
        if x < menor:
            menor = x
    return f"el numero menor es:{menor}"

vector=[]
tam=random.randint(5,20)
vector=llenarListaRandom(vector,tam)
print(vector)
print(menorLista(vector)) 