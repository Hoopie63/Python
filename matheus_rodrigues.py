#lista 1 - Massanori
#Exercicio 1

n1 = int(input('digite n1: '))
n2 = int(input('digite n2: '))
a = n1 + n2
print ('Soma dos numeros é: ', a)
    
#Exercicio 2

metros = float(input('digite o valor em metros: '))
milimetro = metros * 1000
print('valor em milimetros é: ', milimetro)

#Exercicio 3

dias = int(input('digite os dias: '))
horas = int(input('digite o numero de horas: '))
minutos = int(input('digite o numero de minuto: '))
segundos = int(input('digite o numero de segundos: '))
total = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print ('A quantidade de segundos é: ', total)

#Exercio 4

salario = float(input('Digite o valor do seu salario: '))
porcentagem = float(input('digite a porcentagem do aumento: '))
porcentagem = porcentagem / 100
aumento = salario * porcentagem
print(f'o valor do seu aumento foi: {aumento:.2f}')

#Exercicio 5

preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o percentual de desconto: '))
desconto = desconto / 100
desconto = (desconto * preco)
pf = preco - desconto
print(f'o valor final do produto é: {pf:.2f}')

#Exercicio 6

x = float(input('Informe a distancia: '))
vm = float(input('Informe a velocidade media: '))
t = x/vm
print(f'O tempo de viagem será: {t:.2f}')

#Exercicio 7

c = float(input('Informe a temperatura em celsius: '))
f = (c * 1.8) + 32 
print(f'o valor da temperatura em fahrenheit é: {f:.2f}')

#Exercicio 8

f = float(input('Informe a temperatura em fahrenheit: '))
c = (f - 32)/ 1.8
print(f'o valor da temperatura em celsius é: {c:.2f}')

#Exercicio 9

distancia = float(input('informe a distancia que o carro percorreu: '))
dias = float(input('informe os dias que o carro foi usado: '))
preco = (0.15 * distancia) + (60 * dias)
print(f'o valor do aluguel foi: {preco:.2f}')

#Exercicio 10

cigarro = int(input('informe a quantidade de cigarros fumados por dia: '))
anos = int(input('Informe a quantos anos você fuma: '))
total = cigarro * anos * 365
tempo_perdido =  total / 144
print('você perdera ', tempo_perdido ' dias de vida')

#Exercicio 11

input(len(str(2*10**6)))












