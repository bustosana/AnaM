import random
import statistics
   
def generar_arreglo(lista,cantidad):
    lista=[]
    num=0
    for i in range(cantidad):
        num=random.randint(5,20)
        lista.append(num)
    return lista
   

def suma(cantidad,lista):
    lista=[]
    for x in lista:
        if x > sum:
            sum = x
    return f"la suma es:{sum}"

def promedio(cantidad,lista):
     lista=[]
     for i in range(cantidad):
        num=random.randint(5,20)
        lista.append(num)
        return f"elpromedio es:{promedio}"

def mayor(cantidad,lista):
    lista=[]
    for i in range(cantidad):
        num=random.randint(5,20)
        lista.append(num)
    for x in lista:
        if x > mayor:
            mayor = x
    return f"el numero mayor es:{mayor}"

def menor(cantidad,lista):
     lista=[]
     for x in lista:
        if x < menor:
            menor = x
     return f"el numero menor es:{menor}"

def ordenar_ascendente(x,y):
    return x + y

def ordenar_descendente(x,y):
    return x + y

def moda(x,y):
    return x + y

def mediana(cantidad,lista):
     lista=[]
     for i in range(cantidad):
        num=random.randint(5,20)
        lista.append(num)
     return f"la mediana es:{mediana}"
sel=1
while sel !=5:
    print("1-suma")
    print("2-promedio")
    print("3-mayor")
    print("4-menor")
    print("5-orden_ascendente")
    print("6-orden_descendente")
    print("7-moda")
    print("8-mediana")
    print("9-salida")
    sel=int(input("seleccione opcion"))

vector=[]
tam=random.randint(5,20)
vector=generar_arreglo (vector,tam)
print(vector)   

match sel:
    case 1: 
        print(suma(vector))
    case 2: 
        print(promedio(vector))
    case 3:
        print(mayor(vector))
    case 4:
        print(menor(vector))
    case 5:
        print(ordenar_ascendente(vector))
    case 6:
        print(ordenar_descendente(vector))
    case 7:
        print(moda(vector))
    case 8:
        print(mediana(vector))
    