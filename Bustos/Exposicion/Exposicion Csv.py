import csv

with open('Datoss.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)





#Agregar filas al archivo csv

nuevas_filas = [
    ["Pedro", 35, "Programador"],
    ["Ana", 22, "Diseñadora"],
    ["Luis", 30, "Gerente"]
]

# Abrir el archivo CSV en modo de adición ('a')
with open('Datoss.csv', mode='a', newline='', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    writer.writerows(nuevas_filas)
    print()



with open('Datoss.csv', 'r',"newline:", encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)