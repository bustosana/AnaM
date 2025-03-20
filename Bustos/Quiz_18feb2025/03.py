#multiplos de 7 
num = int(input("introduce el numero"))

#encontrar los multiplos de 7
multiplos = [i for i in range (1, num + 1)if num % i == 0]

#mostrar los multiplos 
print(f"los multiplos de {num} son: {multiplos}")