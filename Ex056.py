"""
Exercício Python 56: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

total_idade = 0
total_F = 0
total_M = 0

for informações in range(1, 3):
    sexo = str(input('Digite o sexo da {}ª pessoa (M = Masculino e F = Femenino: ): '.format(informações))).upper()
    #nome = str(input('Digite o nome da {}ª pessoa: '.format(informações))).title()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(informações)))
    print('=-' * 26)

    # primeira condição para masculino
    if sexo == 'M':
        total_M = total_M + 1  # Total de homens
