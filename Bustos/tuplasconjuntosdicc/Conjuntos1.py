import random 

conjunto={1}
print(type(conjunto))
conjuntos2=set([1,2,4])
lista=[random.randint(1,10)for i in range(20)]
print(type(lista))
conjunto3=set(lista)
print(type(conjunto3))
print(conjunto3)

conjunto.update(lista)
print(f"conjunto despues de update")
print(f"{conjunto}") 