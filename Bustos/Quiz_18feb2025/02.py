#solicitar al usuario 2 numeros 
num1 = int(input("introduce el primer numero"))
num2 = int(input("introduce el segundo numero"))

#rectificar si el numero es mayor o menor 
if num1 < num2:
    print("serie ascendente")
    while num1 <= num2:
        print(num1, end= "  ")
        num1 +=1
else: 
    print("descendente")
    while num1 >= num2:
        print(num1, end=   "")
        num1 -=1 