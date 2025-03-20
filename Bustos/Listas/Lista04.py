#hallar el menor de una lista 
def encontrar_menor(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor
numeros = [5, 12, 55, 80, 99]
menor = encontrar_menor(numeros)
print("El número menor es:", menor)