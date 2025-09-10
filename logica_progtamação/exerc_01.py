''' Lista 1 '''
# 01
print('alo mundo')

# 02
num = int(input('digite um número: '))
print('o número escolido foi:', num)

# 03
a = int(input('valor 1: '))
b = int(input('valor 2: '))
soma = a +b 
print('a soma é:', soma)

# 04
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))
media = (n1 +n2 +n3 +n4)/4
print('sua média foi:', media)

# 05
metro = float(input('qual o metro: '))
cm = metro *100
print(cm, 'centímetros')

# 06
import math
pi = math.pi
raio = float(input('qual o valor do raio: '))
area = pi * (raio**2)
print('a aréa é de:', area )

# 07
a = float(input('qual tamanho do lado: '))
area = a**2
print('o dobro da área é', area*2)

# 08
trabalho= float(input('quanto você ganha por hora: '))
hora= float(input('qunatas horas de trabalho por mês: '))
salario= trabalho* hora
print('por mês você ganha', salario) 

# 09
f= float(input('quantos fahrenheit: '))
c= 5* ((f-32)/9)
print(c,'celsius')

# 10
c= float(input('quantos celsius: '))
f= (c* (9/5))+ 32
print(f,'fahrenheit')

# 11
a = int(input('valor 1 [inteiro]: '))
b = int(input('valor 2 [inteiro]: '))
c = float(input('valor 3 [real]: ').replace(',','.'))
q_1 = (a*2)*(b/2)
q_2 = a*3 + c
q_3 = c**3
print(q_1)
print(q_2)
print(q_3)

# 12
g = int(input('quantos gigabytes: '))
meg= g*1024
print(meg, 'megabytes')

# 13
g = int(input('quantos gigabytes: '))
meg= g*1024
kil= g*1048576
print(meg, 'megabytes')
print(kil, 'kilobytes')

# 14
peixe = float(input('quantos quilos tem: '))
peso = peixe -50
if peso >= 0 :
    multa = peso *4
    print('valor da multa:', multa)
else:
    print('continue pescando ')

# 15
trabalho= float(input('quanto você ganha por hora: '))
hora= float(input('qunatas horas de trabalho por mês: '))
salario = trabalho* hora
desconto = salario - (salario* 11/100) - (salario* 8/100) - (salario* 5/100)
print('você irá receber:', desconto)

# 16
lata_tinta = 18 #litros
parede = float(input('qual tamanho da área: ').replace(',','.'))

capacidade_tinta = parede *3 #1 litro pinta 3 paredes
if capacidade_tinta > lata_tinta : # a parede é maior que o tanto de tinta
    lata_tinta += lata_tinta
    
lata = lata_tinta/18
valor = lata * 80

print('o tocal de latas é:', lata, 'o total gasto é:', valor )

# 17


# 18
mbyte_arquivo= float(input('qual o tamanho do arquivo [em MB]: '))
mbits = mbyte_arquivo* 8

velocidade = float(input('qual a velocidade da internet [em Mbps]: '))
tempo = mbits* velocidade
minutos = tempo// 60
print('você precisa esperar uns',minutos, 'minutos') 