# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, conforme a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER

# leia o ano de nascimento de um atleta

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))

# conforme a idade (verificar a idade)

ano_atual = date.today().year
idade = ano_atual - ano_nascimento


# mostrar sua categoria, conforme a idade:

print('Você tem {} anos.'.format(idade))

if idade <= 9:
    print('Sua categoria é: MIRIM.')

elif 9 < idade <= 14:
    print('Sua categoria é: INFANTIL.')

elif 14 < idade <= 19:
    print('Sua categoria é: JÚNIOR')

elif 19 < idade <= 25:
    print('Sua categoria é: SÊNIOR')

elif idade > 25:
    print('Sua categoria é: MASTER')
