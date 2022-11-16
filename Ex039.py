# Exercício Python 39: faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Biblioteca de datatime com import de date

from datetime import date

# ler o ano de nascimento.

ano_nascimento = int(input('Digite sua idade: '))

# verificar o ano atual.

ano_atual = date.today().year

# Verificar a idade.

idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))

# Fez 18:
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade > 18:
    tempo_passou = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(tempo_passou))
    print(f'Seu alistamento foi em {ano_atual - tempo_passou }.')

else:
    tempo_passou = 18 - idade
    print('Ainda faltam {} ano/anos para o alistamento.'.format(tempo_passou))
    print(f'Seu alistamento será em {ano_atual + tempo_passou}.')
