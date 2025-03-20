import random

def rebanadas (lista, ini, fin):
    if ini>len(lista) or fin<len(lista)*-1:
        return "fuera del rango de la lista"
   
    else:
        return lista[ini:fin]
    
def llamarlistarandom(lista):
    lista=[]
    cantida = random.randint(5,20)
    num=0
    for i in range (cantida):
        num=random.randint(1,100)
        lista.append(num)
        return lista
    
vector =[]
vector = llamarlistarandom(vector)
print(vector)
rebi = rebanadas(vector, 2,4)
print(rebi)