numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print(f"A tupla {numeros} contém {pares} números pares e {impares} números ímpares.")
