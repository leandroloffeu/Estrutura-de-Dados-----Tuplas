tupla = (1,2,3,4,5,6,7,8,9,10)
lista = []

for i in tupla:
    if i != 10:
        lista.append(i)

t= tuple(lista) 

print(t)
