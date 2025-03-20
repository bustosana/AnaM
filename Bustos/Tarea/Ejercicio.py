num=int(input("rango del numero aleatorio:"))
import random 
numale = random.randint(1,num)
def funci():
    print("ADIVINA EL NUMERO")

def adivina():
    intentos = 0
    while True:
        numusuario = int(input("ingrese un numero dentro del rango elejido:")) 
        if numusuario > numale:
            intentos += 1
            print ("el numero a acertar es mas pequeño, vuelva a intentar")
        elif numusuario< numale:
            intentos +=1
            print("el numero a acertar es mas grande, vuelva a intentar")
        else:
            print(f"MUY BIEN ACERTASTE, EL NUMERO ERA EL: {numale}, numero de intentos fue de:{intentos}")
            break
funci()
adivina()