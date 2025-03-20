def sumar(x,y):
    return x + y

def restar(x,y):
    return x - y

def multiplicacion(x,y):
    return x * y

def division(x,y):
    return x / y


print("1-sumar")
print("2-restar")
print("3-multiplicar")
print("4-dividir")
print("5-salida")


sel = int(input("seleccionar una opcion"))
num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese un numero"))
match sel:
    case 1:
        print("sum" (num1 + num2))
    case 2:
        print("restar" (num1 + num2))
    case 3: 
        print("multiplicar" (num1 + num2))
    case 4:
        print("dividir" (num1 + num2))
    case 5:
        print("opcion equivocada")

def sumar(x,y):
    return x + y
sel = 1
while sel!= 1: 
    print("1-sumar")
sel = int(input("seleccione una opccion"))

num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese un numero"))
print("la suma es:", sumar(num1,num2))

import random 
n = int(input("ingrese el numero del elemento"))

arreglo = []

for i in range(n): 
    numero_aleatorio = random.randint(5,20)
    arreglo.append(numero_aleatorio) 
suma = sum(arreglo)

print("arreglo generado:", arreglo)
print("la suma de los elementos es:", suma)