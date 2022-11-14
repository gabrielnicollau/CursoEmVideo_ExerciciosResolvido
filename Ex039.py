# Exercício Python 39: faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Biblioteca de datatime com import de date

from datetime import date

# ano de nascimento:

nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year  # pegar o ano atual.
sua_idade = ano_atual - nascimento  # ano atual menos sua data de nascimento.


# Menor de 18:
if sua_idade < 18:
    falta = 18 - sua_idade  # O resultado é o tempo que falta para seu alistamento x anos.
    vai_ser = falta + ano_atual  # Para saber quando vai se alistar.
    print('Você ainda não tem idade para se alistar.')
    print('Você tem {} anos e faltam {} ano/anos para o seu alistamento.'.format(sua_idade, falta))
    print('Seu alistamento vai ser em {}.'.format(vai_ser))

elif sua_idade == 18:
    print('Você está na idade de se alistar!')

else:
    passou = sua_idade - 18
    deveria = ano_atual - passou  # Para saber quando deveria ser alista.
    print('Você já deveria ter se alistado! Se passaram {} anos.'.format(passou))
    print('Deveria ter se alistado no ano de {}.'.format(deveria))
