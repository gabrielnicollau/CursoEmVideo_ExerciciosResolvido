"""
Exercício Python 67: faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

núm = 0
cont = 0

while True:
    núm = int(input('Qual tabuada você quer ver ? '))

    if núm < 0:
        break

