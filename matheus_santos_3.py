#lista_III
'''Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.'''

nota = int(input('digite uma nota de 0 a 10: '))
while nota > 10:
	print ('nota maior que 10 !!!')
	nota = int(input('digite uma nota de 0 a 10: '))
	if nota <= 10:
		break
while nota < 0:
	print ('nota menor que 10 !!!')
	nota = int(input('digite uma nota de 0 a 10: '))
	if nota >= 0:
		break
print ('Nota %d' %nota)

'''Faça um programa que leia um nome de usuário e a 
sua senha e não aceite a senha igual ao nome do 
usuário, mostrando uma mensagem de erro e voltando 
a pedir as informações.'''

usuario = input('digite um nome de usuário: ')
senha = input('digite uma senha: ')

while usuario == senha:
	print ('erro a senha igual a usuário !!!')
	usuario = input('digite um nome de usuário: ')
	senha = input('digite uma senha: ')
	if usuario != senha: 
		break
print ('cadastro efetuado com sucesso')

''' Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

a = int(80000)
b = int(200000)
ano = 0
while a < b:
	a = a + (a * 0.03)
	b = b + (b * 0.015)
	ano = ano + 1
	if a >= b:
		break
print ('A população da cidade A sera maior a cidade B em %d anos' %ano)
print ('A população da cidade A será de: ',a)
print ('A população da cidade B será de: ',b)

'''A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de
então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia
um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.'''

x = int(input('digite um numero inteiro: '))
aurea = 1.618034
raizq = x ** (1/2)
fb = ((aurea ** x) - ((1 - aurea) ** x)) / raizq
print (f'a posição do numero {x} na sequencia de Fibonacci é {fb:.1f}:')

'''Dados dois números inteiros positivos, determinar o máximo divisor comum entre
eles usando o algoritmo de Euclides.'''

a = int(input('digite um numero inteiro: '))
b = int(input('digite o segundo numero inteiro: '))

while a % b != 0:
	a, b = b, a % b
print ('mdc = %d' %b)  
