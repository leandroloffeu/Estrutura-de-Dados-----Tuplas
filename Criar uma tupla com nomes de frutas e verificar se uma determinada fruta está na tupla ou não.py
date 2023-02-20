tupla = ('uva','banana','maça','laranja','goiaba')

v = str(input('digite um nome da fruta para verificar se existe na tupla: '))
if v in tupla:
    print(f'fruta {v} cadastrada!')
else:
    print(f'fruta {v} não cadatrada!')