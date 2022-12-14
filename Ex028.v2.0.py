"""
Exercício Python 58: melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Contudo,
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint  # Módulo para gerar número inteiro aleatório.
contador = 0  # Contador
computador = randint(0, 10)  # Fazer o computador gerar um número aleatório.

print('=-' * 31)
print('Estou pensando em um número entre 0 e 10. Tente adivinhar...')
print('=-' * 31)

jogador = int(input('Em que número eu pensei ? '))  # Escolha do jogador.
contador = contador + 1  # Contador para saber quantas vezes você tentou adivinhar.
while computador != jogador:  # Enquanto o número digitado e a escolha do computador forem diferentes.
    contador = contador + 1  # Contador vai contar + 1.

    if computador != jogador:
        if jogador > computador:
            print('MENOS... Tente mais uma vez.')


        else:
            print('MAIS... Tente mais uma vez')
    jogador = int(input('Em que número eu pensei ? '))

print('\033[32mACERTOU!\033[m Foram {} tentativas.'.format(contador))

"""
Podemos fazer: 
acertou = False
while not acertou:
    jogador = int(input('qual pensei ? '))
        acertou = True
"""