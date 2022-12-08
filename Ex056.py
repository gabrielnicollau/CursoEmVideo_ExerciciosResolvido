"""
Exercício Python 56: desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

soma_idade = 0  # Total da soma.
total_idade = 0  # Total da idade.
maior = 0  # Idade.
nomeHomemMais_Velho = ''  # Armazenar o nome que for maior.
total_mulheres = 0


for informações in range(1, 5):
    print('-' * 16, '{}'.format(informações), '-' * 16)
    nome = str(input('Digite o nome da pessoa: ')).title()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M / F]: ')).upper()

    soma_idade = soma_idade + idade  # Soma da idade.
    total_idade = soma_idade / 4  # Média de idade.

    if sexo == 'M' and idade > maior:  # Se for masculino e a variável idade é maior que variável maior que é zero.
        maior = idade  #  Então o maior que é zero recebe a idade.
        nomeHomemMais_Velho = nome  # e variável nomeHomemMais_Velho recebe o nome da pessoa, um ligado no outro.

    if sexo == 'F' and idade < 20:  # Se for femenina e menor que 20 anos.
        total_mulheres = total_mulheres + 1

print('')
print('A média de idade dos integrandes são de {:.0f} anos.'.format(total_idade))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(nomeHomemMais_Velho, maior))
print('Existem {} mulheres que tem a idade inferior a 20 anos.'.format(total_mulheres))
