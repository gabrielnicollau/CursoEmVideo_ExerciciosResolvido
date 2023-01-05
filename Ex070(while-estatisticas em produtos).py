"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print('-' * 40)
print('            LOJA DO BILHEU')
print('-' * 40)

total_gasto = 0
totMaior_mil = 0
menor_preço = 0
cont_product = 0

while True:
    nome_produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont_product += 1
    total_gasto += preço  # Total gasto

    if preço > 1000:
        totMaior_mil += 1

    resposta = ' '
    while resposta not in 'SN':
        print('-' * 30)
        resposta = str(input('Quer continuar [S/N]? ')).title().split()[0]

    if cont_product == 1:
        menor_preço = preço  # O primeiro valor vai ser colocado na variável "menor_preço".

    else:
        if preço < menor_preço:  # Se o valor que tiver dentro da váriavel "preço" for menor que valor da variável "menor_preço".
            menor_preço = preço  # A váriavel "menor_preço" vai ser atualizada com o menor valor que tive no variável preço.

    if resposta == 'N':  # Condição para encerrar o programa.
        break

print('')  # Pular linha.
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compras foi de R${total_gasto:.2f} reais.')
print(f'Temos {totMaior_mil} produtos custando mais de R$1.000 reais.')
print(f'O produto mais barato custou R${menor_preço:.2f} reais.')
