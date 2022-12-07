"""
Exercício Python 55: faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lidos.
"""

lista = []  # Adicionar o peso das pessoas em uma lista.

for pessoas in range(1, 6):
    peso = float(input('Digite o peso(Kg) da {}ª pessoa: '.format(pessoas)))  # Ler o peso de 5 pessoas.
    lista.append(peso)  # Adicionar os pesos das pessoas na lista, usar o append para isso.

print('O MAIOR PESO É {}Kg'.format(max(lista)))  # maior para mostrar o maior peso na lista.
print('O MENOR PESO É {}Kg'.format(min(lista)))  # min para mostrar o menor peso dentro da lista.

'''
Podemos fazer também de um outro jeito:
maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Digite o peso(Kg) da {}ª pessoa: '.format(pessoas)))  # Ler o peso de 5 pessoas.
    if pessoa == 1:
        maior = peso
        menor = peso
        
    else:
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso
            
print('O MAIOR PESO É {}Kg'.format(maior))  # maior para mostrar o maior peso na lista.
print('O MENOR PESO É {}Kg'.format(menor))  # min para mostrar o menor peso dentro da lista.
'''