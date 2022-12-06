"""Exercício Python 53: crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
espaços. Exemplos de palíndromos:

APOS A SOPA.
A SACADA DA CASA.
A TORRE DA DERROTA.
O LOBO AMA O BOLO.
A NOTARAM A DATA DA MARATONA.
"""

frase = str(input('Digite uma frase: '))  # Sua frase.
frase_condições = frase.upper().strip().split()  # Condição para python analisar a frase sem problemas(usuário).
sem_espaço = ''.join(frase_condições)  #''.join juntar a frase toda em uma.
frase_invertida = sem_espaço[::-1]  # Inverter a frase ::-1 da direita para a esquerda.

if sem_espaço == frase_invertida:  # Condição se a frase invertida for igual à frase digitada, então é palíndromo.
    print('A frase digitada \033[4:34m{}\033[m invertida fica \033[33m{}\033[m, \033[32mÉ UM PALÍNDROMO!\033[m'.format(frase, frase_invertida))
else:
    print('A frase digitada \033[4:31m{}\033[m invertida fica \033[33m{}\033[m, \033[31mNÃO É PALÍNDROMO!\033[m'.format(frase, frase_invertida))

'''
inverso = ''
Podemos usar o range para inventer a frase
for letra in range(len(sem_espaço) -1, -1, -1): -----> (primeira letra)-1, (última letra) -1, (voltando uma letra)-1.
    inverso += sem_espaço[letra]
'''
