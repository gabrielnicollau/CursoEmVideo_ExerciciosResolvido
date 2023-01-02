"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag).
"""

numero = 0  # Input de número começa com 0.
cont_total = 0  # Valor total começa com 0.
cont_numeros = 0  # Quantidade de números digitados começa com 0.

while numero != 999:  # Enquanto o input do número não receber o valor 999, vai ficar em loop.
    numero = int(input('Digite um valor [999 para encerrar]: '))  # Input para número
    if numero != 999:  # Se número for diferente de 999, não for digitado, vai executa esse if. Caso seja, vai sair do if.
        cont_numeros += 1  # Total de números digitados
        cont_total = cont_total + numero  # Total de números.
print('Você digitou {} número e a soma entre eles é {}.'.format(cont_numeros, cont_total))
print('FIM!')
