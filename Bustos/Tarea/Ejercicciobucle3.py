def primos(num):
    divi = [i for i in range(2,num) if num % i == 0]
    return len(divi) == 0

num_primo = [num for num in range(1, 1001)
                    if primos(num)]
print(f"los numeros primos del 1 al 1000 son: {num_primo}")