#sumar los elementos de una lista que ya este llena
def sumar_elementos(lista):
    suma = sum(lista)
    return suma

numeros = [8, 15, 25, 75, 80]
resultado = sumar_elementos(numeros)
print("La suma de los elementos es:", resultado)
