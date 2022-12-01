"""Exercício Python 48: faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
encontram no intervalo de 1 até 500."""

# Execute o programa, play!

# Gerar número de 1 até 500.

# múltiplos até 10
# múltiplos de 3 o resto da divisão é 0
# 3, 6, 9 == 3 e 9 são ímpares e 6 é par.

cont_ímpares = 0  # Contador de números ímpares.
cont = 0

for numero in range(1, 501):  # Range de 1 até 500.
    if numero % 3 == 0:  # Resto do número divido por 3 for igual a 0, é divisível por 3
        if numero % 2 == 1:
            cont = cont + 1  # Contador: vai contar mais 1 que eu achei, ou seja, números ímpares divisíveis.
            cont_ímpares = cont_ímpares + numero  # Acumulador: Achar um número divisível por 0 vai acumular os valores
            # e vai soma-los.

print('A soma dos {} valores é: {}'.format(cont, cont_ímpares))
