#hallar la varianza de una lista 
def calcular_varianza(lista):
    n = len(lista)  
    if n == 0:
        return None
    
    media = sum(lista) / n 
    suma_diferencias = sum((x - media) ** 2 for x in lista)  
    varianza = suma_diferencias / n  
    
    return varianza

numeros = [8, 4, 55, 15, 7]
print("La varianza es:", calcular_varianza(numeros))