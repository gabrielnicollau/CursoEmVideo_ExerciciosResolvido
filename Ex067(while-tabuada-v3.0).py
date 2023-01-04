"""
Exercício Python 67: faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:  # loop infinito.

    núm = int(input('Qual tabuada você quer ver ? '))

    print('-' * 30)

    if núm < 0:
        break

    for tabuada in range(1, 11):
        print(f'{núm} x {tabuada:2} = {núm * tabuada}')

    print('-' * 30)
print('PROGRAMA ENCERRADO!')
