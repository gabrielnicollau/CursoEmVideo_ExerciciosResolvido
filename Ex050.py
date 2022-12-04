"""Exercício Python 50: desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o."""

print('Digite os seis valores (um por vez).')
print('=-' * 18)
cont = 0  # contador de números pares que existem.
total = 0  # contador de soma, vai somar os valores pares que existem.
for controlador in range(1, 7):  # range de 1 até 7.
    numero = int(input('Digite o {}° valor: '.format(controlador)))  # variavel vai repetir 7 vezes e pegar os valores.
    if numero % 2 == 0:  # número dividido por 2 e restar 0 é par.
        cont = cont + 1  # Vai contar quantos números pares existem, ou seja, o resto da divisão é 0.
        total = total + numero  # Vai somar somente os valores pares.

print('Existe no total {} números PARES e a soma deles é {}.'.format(cont, total))
