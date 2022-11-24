# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
#
# — à vista no cartão: 5% de desconto
#
# –em até 2x no cartão: preço formal
#
# — 3x ou mais no cartão: 20% de juros

########################################################################################################################

from time import sleep

# Layout
print('=-' * 7, 'FORMAS DE PAGAMENTO', '-=' * 7)

preço = float(input('\033[33mDigite o valor da compra R$:\033[m '))

# Layout da formas de pagamento.

print('\33[33mESCOLHA UMA FORMA DE PAGAMENTO\033[m')
print('''
À vista dinheiro/cheque - \033[34m[ 1 ]\033[m
À vista no cartão - \033[35m[ 2 ]\033[m
2x no cartão - \033[36m[ 3 ]\033[m
3x ou mais no cartão - \033[37m[ 4 ]\033[m''')

# Escolha do cliente e valor da compra.

escolha = int(input('\033[33mQual sua escolha de pagamento ?\033[m '))

# à vista dinheiro/cheque: 10% de desconto
if escolha == 1:
    desconto = preço - (preço * 10 / 100)

    print('\033[37mCALCULANDO...\033[m')
    sleep(1.0)

    print('Sua compra de \033[32mR${:.2f}\033[m vai sair por \033[32mR${:.2f}\033[m no final.'.format(preço, desconto))

# à vista no cartão: 5% de desconto

elif escolha == 2:
    desconto_cartão = preço - (preço * 5 / 100)

    print('\033[37mCALCULANDO...\033[m')
    sleep(1.0)

    print('Sua compra de \033[32mR${:.2f}\033[m pagando à vista no cartão'.format(preço), end=' ')
    print('Vai sair por \033[32mR${:.2f}\033[m.'.format(desconto_cartão))

# em até 2x no cartão: preço formal

elif escolha == 3:
    parcelado2 = preço / 2

    print('\033[37mCALCULANDO...\033[m')
    sleep(1.0)

    print('Sua compra será parcela em\033[32m 2x de R${:.2f}\033[m'.format(preço), end=' ')
    print('vai sair por \033[32mR${:.2f}\033[m SEM JUROS.'.format(parcelado2))

elif escolha == 4:
    parcelas = int(input('\033[33mQuantas vezes será parcela (limite de até 12 vezes):\033[m '))

    juros = preço + (preço * 20 / 100)  # Calcular 20% do preço e somar com o preço inicial para descobrir os juros.
    total_parcelas = juros / parcelas  # Dividi os juros pela quantidade de parcelas.

    print('\033[37mCALCULANDO...\033[m')
    sleep(1.0)

    print('Sua compra será parcelada em \033[4:34m{}x de R${:.2f} COM JUROS\033[m.'.format(parcelas, total_parcelas))
    print('Sua compra foi de \033[32mR${:.2f}\033[m e \033[4:31mvai ficar custando R${:.2f}\033[m.'.format(preço, juros))


else:
    escolha = 0
    print('\033[31mFORMA DE PAGAMENTO INVÁLIDA!\033[m')
