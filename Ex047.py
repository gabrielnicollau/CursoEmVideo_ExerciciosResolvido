"""Exercício Python 47: Crie um programa que mostre na tela todos os números pares no intervalo entre
1 e 50."""

# iniciar

iniciar = str(input('Digite iniciar para executar o programa: ')).strip().title()

print('=-' * 20)
print('\033[31mVermelho\033[m é impar.')
print('\033[32mVerde\033[m é par.')
print('=-' * 20)

# Um número inteiro é par se ele é divisível por 2, ou seja, se a divisão desse número por 2 tem resto igual a 0.

if iniciar == iniciar:
    for contador in range(1, 51):
        if contador % 2 == 0:
            print('\033[32m{}\033[m'.format(contador), end=' ')
        else:
            print('\033[31m{}\033[m'.format(contador), end=' ')
print('FIM!')
