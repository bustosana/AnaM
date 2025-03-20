def encontrar_mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
numeros = [72, 55, 85, 8, 18, 555]
mayor = encontrar_mayor(numeros)
print("El número mayor es:", mayor)