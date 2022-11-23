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

# Layout da formas de pagamento.

print('\33[33mESCOLHA UMA FORMA DE PAGAMENTO\033[m')
print('''
\033[34m[ 1 ]\033[m à vista dinheiro/cheque
\033[35m[ 2 ]\033[m à vista cartão
\033[36m[ 3 ]\033[m 2x no cartão
\033[37m[ 4 ]\033[m 3x ou mais no cartão''')

# Escolha do cliente e valor da compra.

escolha = int(input('\033[33mQual sua escolha de pagamento ?\033[m '))
valor = float(input('\033[33mDigite o valor da compra R$:\033[m '))

print('\033[31mCalculando...\033[m')
sleep(1.5)
# à vista dinheiro/cheque: 10% de desconto
if escolha == 1:
    desconto = valor - (valor * 10 / 100)
    print('Sua compra de \033[32mR${:.2f}\033[m vai sair por \033[32mR${:.2f}\033[m no final.'.format(valor, desconto))

# à vista no cartão: 5% de desconto

elif escolha == 2:
    desconto_cartão = valor - (valor * 5 / 100)
    print('Sua compra de \033[32mR${:.2f}\033[m pagando à vista no cartão'.format(valor), end='')
    print(' vai sair por \033[32mR${:.2f}\033[m.'.format(desconto_cartão))

# em até 2x no cartão: preço formal

elif escolha == 3:
    parcelado2 = valor / 2
    print('Sua compra de \033[32mR${:.2f}\033[m'.format(valor), end='')
    print(' vai sair por \033[32mR${:.2f}\033[m.'.format(parcelado2))

elif escolha == 4:
    vezes = int(input('Quantas vezes será parcela (limite de até 12 vezes): '))
    print('\033[31mCalculando...\033[m')
    sleep(1.5)
    parcelado3 = valor / vezes
    print('Sua compra de \033[32mR${:.2f} parcelado em {}x'.format(valor, vezes), end='')
    print(' vai sair por \033[32mR${:.2f}\033[m.'.format(parcelado3))
