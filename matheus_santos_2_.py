#Lista_II
 
#Exercicio_1

lado_1 = int(input('Digite o valor do lado a: '))
lado_2 = int(input('Digite o valor do lado b: '))
lado_3 = int(input('Digite o valor do lado c: '))
#A soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado
if (lado_1 + lado_2) < lado_3 or (lado_1 + lado_3) < lado_2 or (lado_2 + lado_3) < lado_1 :
	print ('Não pode ser um triângulo')
	print ('Um dos lados é maior que a soma dos outros')
#equilátero: possui os três lados iguais
elif lado_1 == lado_2 == lado_3:
	print('Seu triangulo é equilátero')
#isósceles: possui dois lados com medidas iguais
elif lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1
	print('Seu triangulo é isósceles')
#escaleno: possui os três lados com medidas diferentes
else :
	print('Seu triangulo é escaleno')

	pass

#Exercicio_2

ano = int(input('Digite o ano: '))
#Situações para o ano ser bissexto
#se for uma divisão exata por 4, deve-se vericar então se não é divisivel por a 100
if (ano % 4 == 0) and (ano % 100 != 0):
		print('O ano é bissexto !!!')
#se não for uma divisão exata por 4, mas por 400 for ele é bissexto
elif (ano % 4 != 0) and (ano % 400 == 0):
	print('O ano é bissexto !!!')
#Se não for ambos, então ...
else:
	print('O ano não é bissexto :(')

	pass

#Exercicio_3
#receber peso do peixe
peso = float(input('Informe o peso do peixe: '))

if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print(f'O peso do seu peixe excedeu em {excesso:.2f} e o valor da multa é {multa:.2f} ')
else:
	excesso = 0
	multa = 0 
	print('multa = ', multa, ' excesso = ', excesso)
	
#Exercicio_4
#Faça um Programa que leia três números e mostre o maior deles. 
numero_1 = int(input('Informe o primeiro numero: '))
numero_2 = int(input('Informe o segundo numero: '))
numero_3 = int(input('Informe o terceiro numero: '))
if numero_1 >= numero_2 and numero_1 >= numero_3: #if a >= b and a >= c: maior a
	print ('numero ', numero_1, ' é o maior ')
elif numero_2 >= numero_3: #elif b >= c: maior b
	print ('numero ', numero_2,' é o maior')
else: #maior c
	print('numero ', numero_3,' é o maior')


#Exercicio_5
#Faça um programa que leia três números e mostre o maior deles e o menor deles
numero_1 = int(input('Informe o primeiro numero: '))
numero_2 = int(input('Informe o segundo numero: '))
numero_3 = int(input('Informe o terceiro numero: '))
if numero_1 >= numero_2 and numero_1 >= numero_3:
	print ('O numero %d é o maior' %numero_1)
elif numero_2 >= numero_3:
	print ('O numero %d é o maior' %numero_2)
else:
	print('O numero %d é o maior' %numero_3)
if numero_1 <= numero_2 and numero_1 <= numero_3:
	print ('O numero %d é o menor' %numero_1)
elif numero_2 <= numero_3:
	print ('O numero %d é o menor' %numero_2)
else:
	print ('O numero %d é o menor' %numero_3)

#Exercicio_6
# quanto você ganha por hora e o número de horas trabalhadas no mês.
qnt_ganho = float(input('Informe o quanto você ganha por hora: '))
num_horas = int(input('Informe o numero de horas trabalhadas no mês: '))
total_salario_bruto = qnt_ganho * num_horas
imposto_renda = 0.11 * total_salario_bruto  
inss = 0.08 * total_salario_bruto
sindicato = 0.05 * total_salario_bruto
total_salario_liquido = total_salario_bruto - imposto_renda - inss - sindicato
print (f'O seu salario bruto é de: {total_salario_bruto:.2f}')
print (f'O valor do imposto renda cobrado é: {imposto_renda:.2f}')
print (f'O valor do INSS cobrado é: {inss:.2f}')
print (f'O valor do sindicato cobrado é: {sindicato:.2f}')
print (f'O valor do seu salario liquido é: {total_salario_liquido:.2f}')

#Exercicio_7
# O programa deverá pedir o tamanho em metros quadrados da área 
metros = int(input('Qual o tamanho em m² da área: '))
# a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
if metros % 54 != 0:
	latas = int (metros/ 54) + 1
else:
	latas = metros / 54
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
valor = latas * 80
print('%d lata(s) a um custo de %.2f' %(latas, valor))












































