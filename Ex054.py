"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date  # Biblioteca para pegar o ano atual do computador.

ano_atual = date.today().year  # Ano atual do computador.

contmaior18 = 0  # Contador para pessoas maiores de 18.
contmenor18 = 0  # Contador para pessoas menores de 18.

for pessoas in range(1, 8):  # range de 1 até 7 pessoas
    anos_nascimentos = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))  # variável para guardar o ano de nascimento.
    idades = ano_atual - anos_nascimentos  # Descobrir a idade dessas pessoas.

    if idades >= 18:  # Pessoas maiores ou igual a 18.
        contmaior18 = contmaior18 + 1  # Contador vai adicionar um para cada pessoa que for maior de 18.

    else:  # Pessoas menores de 18.
        contmenor18 = contmenor18 + 1  # Contador vai adicionar um para cada pessoa que for menor de 18.
print('')

print('Existem \033[32m{}\033[m pessoas \033[32mMAIORES DE IDADE\033[m.\n'.format(contmaior18))
print('Existem \033[31m{}\033[m pessoas \033[31mMENORES DE IDADE\033[m.'.format(contmenor18))
