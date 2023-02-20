tupla = (1,2,3,4,5,6,7,8,9,10)

n = int(input('digite um numero para verificar se existe na tupla criada: '))
if  n in tupla:
    print(f'numero {n} consta na tupla!')
else:
    print(f'numero {n} NÃO consta na tupla!')