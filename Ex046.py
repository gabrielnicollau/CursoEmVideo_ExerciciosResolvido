"""Exercício Python 46: faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from time import sleep

play = str(input('Digite (play) para iniciar a contagem regressiva: ')).strip().title()
if play == play:
    for contador in range(10, -1, -1):
        print(contador)
        sleep(1)
print('PA! PA! POW! POW!')
