def pedir_numero():
    return int(input("Ingresa un número: "))

def imprimir_opuesto(num):
    print(f"{num} opuesto {-num}")

def contar():
    contador = 0

    while True:
        num = pedir_numero()
        if num ==0:
            break

        imprimir_opuesto(num)
        contador += 1
    
    print(f"se ingresaron {contador}numeros:")

contar()
