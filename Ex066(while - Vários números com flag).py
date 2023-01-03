"""
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre elas (desconsiderando o flag).
"""

numeros = 0  # Valor começa com 0.
soma = 0  # Soma.
cont = 0  # Contador começa com 0.

while True:  # Enquanto for verdadeiro.
    numeros = int(input('Digite um número [999 para parar]: '))  # Input sendo verdadeiro.

    if numeros == 999:
        break

    soma += numeros  # Soma dos números digitados.
    cont += 1  # contador de quantas vezes foi digitados o número

print(f'Foram digitados {cont} valores e soma deles é {soma}!')
