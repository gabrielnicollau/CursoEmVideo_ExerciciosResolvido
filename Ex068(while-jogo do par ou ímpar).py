"""
Exercício Python 68: faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

cont_v = 1

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    escolha = ' '

    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar [P/I] ? ')).strip().title()[0]


    if escolha == 'P':  # Escolha do jogador foi PAR.
        if total % 2 == 0:
            print(f'O computador jogou {computador} e você jogou {jogador}. O total é {total} PAR!')
            print(f'Você escolheu {escolha}.')
            print(f'VOCÊ GANHOU! Total de vitórias {cont_v}.')
            cont_v += cont_v + 1

            print('-' * 45)

        else:
            print(f'O computador jogou {computador} e você jogou {jogador}. O total é {total} ÍMPAR!')
            print(f'Você escolheu {escolha}.')
            print('VOCÊ PERDEU')
            break

    elif escolha == 'I':  # Escolha do jogador foi ÍMPAR.
        if total % 2 == 1:
            print(f'O computador jogou {computador} e você jogou {jogador}. O total é {total} ÍMPAR!')
            print(f'Você escolheu {escolha}.')
            print(f'VOCÊ GANHOU! Total de vitórias {cont_v}.')

            print('-' * 45)

        else:
            print(f'O computador jogou {computador} e você jogou {jogador}. O total é {total} PAR!')
            print('VOCÊ PERDEU')
            print(f'Você escolheu {escolha}.')
            break
print('FIM!')
