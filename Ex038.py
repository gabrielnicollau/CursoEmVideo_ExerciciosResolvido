# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. Mostrando uma mensagem na tela:

# O primeiro valor é maior

# O segundo valor é maior

# Não existe valor maior, os dois são iguais

# Valor 1 e valor 2

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor:'))

if valor1 > valor2:
    print('O PRIMEIRO valor é maior!')

elif valor2 > valor1:
    print('O SEGUNDO valor é maior!')

else:
    print('Os dois valores são IGUAIS!')