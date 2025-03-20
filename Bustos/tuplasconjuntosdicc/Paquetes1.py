# mi_paquete/__init__.py
print(f"Paquete 'mi_paquete' cargado. __name__ = {__name__}")

# mi_paquete/modulo1.py

def saludar():
    return "¡Hola desde modulo1!"

if __name__ == "__main__":
    print("modulo1 se está ejecutando directamente.")
    print(saludar())
else:
    print(f"modulo1 se ha importado como módulo. __name__ = {__name__}")

# mi_paquete/modulo2.py

def despedir():
    return "¡Adiós desde modulo2!"

if __name__ == "__main__":
    print("modulo2 se está ejecutando directamente.")
    print(despedir())
else:
    print(f"modulo2 se ha importado como módulo. __name__ = {__name__}")

# mi_paquete/main.py

from mi_paquete import modulo1, modulo2 # type: ignore

if __name__ == "__main__":
    print("main.py se está ejecutando directamente.")
    print(modulo1.saludar())
    print(modulo2.despedir())
else:
    print(f"main.py se ha importado como módulo. __name__ = {__name__}")
