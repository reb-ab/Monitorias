''' ARIVIDADE 02 '''

''' EX 1 '''
idade = int(input('qual sua idade: '))
if idade >= 18 :
    print('já pode ser preso')
else :
    print('você está na parte free da vida ainda')


''' EX 2 '''
numero = int(input('escolha um número: '))
par_impar = numero % 2
if par_impar == 0:
    print('o númeor é par')
else :
    print('o número é ímpar')


''' EX 3 '''
idade = int(input('qua sua idade: '))

if idade <= 12:
    print('você é uma criança')
elif 13 <= idade <=17 :
    print('você é um adolecente')
elif 18<= idade <= 59 :
     print('você é um adulto')
else :
    print('você é um velho')


''' EX 4 '''
lado_1 = float(input('lado 1: ').replace(',','.'))
lado_2 = float(input('lado 2: ').replace(',','.'))
lado_3 = float(input('lado 3: ').replace(',','.'))

if lado_1 == lado_2 == lado_3 :
    print('equilátero')
elif lado_1 == lado_2 or lado_1 == lado_3 :
    print('isóceles')
else:
    print('escaleno')


''' EX 5 '''
numero = int(input('escolha um número inteito: '))
if numero <0 :
    print('número negativo')
elif numero == 0 :
    print('nulo')
else:
    print('número positivo')


''' EX 6 '''
nota = int(input('qual sua nota: '))
if nota>= 7 :
    print('você está aprovado')
elif 5 <= nota < 7 :
    print('você está de recuperação')
else :
    print('você está reprovado')


''' EX 7 '''
a = int(input('qaual valor de [a]: '))
b = int(input('qaual valor de [b]: '))
c = int(input('qaual valor de [c]: '))

delta = b**2 - (4*a*c)
if a == 0 :
    print('não é do 2º grau')
elif delta < 0 :
    print('não existe raiz real')
elif delta == 0 :
    print('existe duas raizes iguais')
elif delta > 0 :
    print('existe duas raizes reais')


