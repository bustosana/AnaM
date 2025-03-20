#lista=[10 for i in range(5)]
import random 
lista=[i for i in range (5)]
print(lista)
lista=[i*i for i in range(1,6)]
print(lista)
#tam=random.randint(5,20)
lista=[random.randint(0,100)for i in range (random.randint(5,20))]
print(lista) 

#si el numero es menor que 50 uste va llenar la lista con 1 pero si es mayor que 50 va poner un numero 2 
#si es par entonces doblelo y si en impar halle la mitad 