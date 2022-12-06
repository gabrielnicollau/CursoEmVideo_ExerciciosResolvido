"""Exercício Python 51: desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão."""


print('=-' * 12)
print('\033[33mOS 10 PRIMEIROS TERMOS DE UMA PA\033[m')
print('=-' * 12)

# Precisamos saber quem é o seu primeiro termo e qual a sua razão.

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

# Com o primeiro_termo, a partir dele, somar a razão, vamos encontrar os termos sucessores.
# Exemplo: termo = 4
#          razão = 2
#          a1 = 4
#          a2 = 4+ 2 = 6
#          a3 = 6 + 2 = 8

# Fórmula: an = a1 + (n – 1)r
pa = termo + (10 - 1) * razão  # Fórmula aplicado em python.
for controle in range(termo, pa + 1, razão):  # Laço de repetição e pa + 1 para fazer os 10 termos.
    print('{}'.format(controle), end=' ⇾ ')
print('FIM!')

