#hallar la mediana de una lista
def encontrar_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada) 
    
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        medio1 = lista_ordenada[n // 2 - 1]
        medio2 = lista_ordenada[n // 2]
        return (medio1 + medio2) / 2

numeros = [2, 12, 8, 9, 25]
print("La mediana es:", encontrar_mediana(numeros))