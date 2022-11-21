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

# – Até 9 anos: MIRIM
if idade <= 9:  # Menor que 9
    print('Sua categoria é: MIRIM.')

# – Até 14 anos: INFANTIL
elif idade <= 14:  # Se for maior que 9 vai entrar nesse elif e assim sucessivamente.
    print('Sua categoria é: INFANTIL.')

# – Até 19 anos: JÚNIOR
elif idade <= 19:
    print('Sua categoria é: JÚNIOR')

# – Até 25 anos: SÊNIOR
elif idade <= 25:
    print('Sua categoria é: SÊNIOR')

# – Acima de 25 anos: MASTER
elif idade > 25:
    print('Sua categoria é: MASTER')
