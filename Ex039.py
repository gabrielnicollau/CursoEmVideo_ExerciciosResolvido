# Exercício Python 39: faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Biblioteca de datatime com import de date

from datetime import date

# ler o ano de nascimento

ano_nascimento = int(input('Digite seu ano que nascimento: '))

# conforme a sua idade, se ele ainda vai se alistar ao serviço militar

ano_atual = date.today().year

ano_alistamento = ano_atual - ano_nascimento

print('Você tem {} anos'.format(ano_alistamento))

# Maior de 18

if ano_alistamento == 18:
    print('Está na hora de se alistar!')

# Passou dos 18, calcular quanto tempo já passou.

elif ano_alistamento > 18:
    print('Você tem {} anos')

# Já passou o alistamento

