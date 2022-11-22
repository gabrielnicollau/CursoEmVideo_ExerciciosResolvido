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

# Layout
print('=-' * 7, 'FORMAS DE PAGAMENTO', '-=' * 7)

# Layout da formas de pagamento.

print('ESCOLHA UMA FORMA DE PAGAMENTO')

print('''
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

# Escolha do cliente e valor da compra.

escolha = int(input('Qual sua escolha de pagamento ? '))
valor = float(input('Digite o valor da compra R$: '))

# à vista dinheiro/cheque: 10% de desconto
if escolha == 1:
    desconto = valor - (valor * 10 / 100)
    print('Sua compra de \033[32mR${:.2f}\033[m vai sair por \033[32mR${:.2f}\033[m no final.'.format(valor, desconto))

# à vista no cartão: 5% de desconto

elif escolha == 2:
    desconto_cartão = valor - (valor * 5 / 100)
    print('Sua compra de \033[32mR${:.2f}\033[m pagando à vista no cartão'.format(valor), end='')
    print(' vai sair por \033[32mR${:.2f}\033[m no final.'.format(desconto_cartão))

# em até 2x no cartão: preço formal

elif escolha == 3:
    parcelado2 = valor / 2
    print('Sua compra de \033[32mR${:.2f}\033[m'.format(valor), end='')
    print(' vai sair por \033[32mR${:.2f}\033[m.'.format(parcelado2))

elif escolha == 4:
    vezes = int(input('Quantas vezes será parcela (limite de até 12 vezes): '))
    parcelado3 = valor / vezes
    print('Sua compra de \033[32mR${:.2f} parcelado em {}x')
