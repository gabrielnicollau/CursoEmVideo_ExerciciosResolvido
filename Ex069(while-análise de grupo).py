"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

maior_18 = 0
cont_H = 0
menor_F20 = 0

while True:
    print('-' * 30)
    print('     CADASTRO DE PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [H/F]: ')).title().split()[0]

    if sexo == 'M':
        cont_H += 1

    if idade >= 18:
        maior_18 += 1

    if sexo == 'F' and idade < 20:
        menor_F20 += 1

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N] ? ')).title().split()[0]

    if resposta == 'N':
        break

print('-' * 45)
print(f'Total de pessoas no grupo com mais de 18 anos: {maior_18}')
print(f'Quantidade de Homens cadastrados: {cont_H}')
print(f'Quantidades de mulheres com menos de 20 anos: {menor_F20}')
print()
print('FIM!')
