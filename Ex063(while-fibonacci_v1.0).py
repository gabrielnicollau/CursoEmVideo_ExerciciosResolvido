"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:"""

# Para saber o proximo termo, basta somar o penultimo e ultimo termo da sequência.
# Prox_termo = penultimo + ultimo. O valor dessa soma é o proximo termo.
# 0 - 1 - 1 - 2 - 3 - 5 - 8
# 0 + 1 = 1
# 1 + 1 = 2
# 2 + 1 = 3

print('-' * 55)
print('\033[34mSequência de Fibonacci\033[m')
print('-' * 55)

termo = int(input('Digite quantos termos você quer ver: '))

penultimo = 0  # Primeiro termo da sequência.
ultimo = 1  # Segundo termo da sequência.

print('\033[31m{} ➡ {} \033[m'.format(penultimo, ultimo), end='')

cont = 3  # Contador de termos, inicia no 3 porque já temos os dois primeiro termos (0 e 1 são os dois primeiro padrões).
while cont <= termo:
    prox_termo = penultimo + ultimo  # Variável prox_termo: Para descobrir o proximo termo na sequência temos que somar os dois anteriores.
    penultimo = ultimo  # Quando a primeira sequência se formar, o último termo vai virar penultimo termo.
    ultimo = prox_termo  # E o proximo termo vai virar o último.
    cont += 1  # Encerrar o loop.
    print('\033[32m➡ {} \033[m'.format(prox_termo), end='')
print('\33[33m➡ FIM!\033[m')
