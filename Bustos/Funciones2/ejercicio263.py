from statistics import median

def mitades (lista):
    tam=len(lista)
    print(tam)
    if tam%2!=0:
        m=median(lista)
        lista.append(int(m))
        tam=len(lista)
        print(lista)
    r1=lista[:int(tam/2)]
    r2=lista[int(tam/2):]
    print(f"mitad1= {r1}")
    print(f"mitad2= {r2}")
