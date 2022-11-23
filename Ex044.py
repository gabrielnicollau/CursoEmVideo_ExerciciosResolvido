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

valor = float(input('\033[33mDigite o valor da compra R$:\033[m '))

# Layout da formas de pagamento.

print('\33[33mESCOLHA UMA FORMA DE PAGAMENTO\033[m')
print('''
\033[34m[ 1 ]\033[m à vista dinheiro/cheque
\033[35m[ 2 ]\033[m à vista cartão
\033[36m[ 3 ]\033[m 2x no cartão
\033[37m[ 4 ]\033[m 3x ou mais no cartão''')

# Escolha do cliente e valor da compra.

escolha = int(input('\033[33mQual sua escolha de pagamento ?\033[m '))
print('\033[31mCalculando...\033[m')
sleep(1.0)

# à vista dinheiro/cheque: 10% de desconto
if escolha == 1:
    desconto = valor - (valor * 10 / 100)
    print('Sua compra de \033[32mR${:.2f}\033[m vai sair por \033[32mR${:.2f}\033[m no final.'.format(valor, desconto))

# à vista no cartão: 5% de desconto

elif escolha == 2:
    desconto_cartão = valor - (valor * 5 / 100)
    print('Sua compra de \033[32mR${:.2f}\033[m pagando à vista no cartão'.format(valor), end=' ')
    print('Vai sair por \033[32mR${:.2f}\033[m.'.format(desconto_cartão))

# em até 2x no cartão: preço formal

elif escolha == 3:
    parcelado2 = valor / 2
    print('Sua compra de \033[32mR${:.2f}\033[m'.format(valor), end=' ')
    print('vai sair por \033[32mR${:.2f}\033[m.'.format(parcelado2))



elif escolha == 4:
    parcelas = int(input('\033[33mQuantas vezes será parcela (limite de até 12 vezes):\033[m '))
    print('\033[31mCalculando...\033[m')
    sleep(1.0)

    juros = valor * 20 / 100  # Juros por mês
    parc_juros = (valor / parcelas) + juros
    valor_total = parc_juros * parcelas
    juros_total = juros * parcelas

    print('Sua compra será parcelas em \033[35m{}x de R${:.2f} COM JUROS\033[m.'.format(parcelas, juros))
    print('Valor inicia sem juros \033[33mR${:.2f}'.format(parc_juros), end=' ')
    print('COM JUROS\033[m. O total do valor vai ser \033[32mR${:.2f}\033[m.'.format(valor_total))
    print('Total de \033[31mJUROS é R${:.2f}\033[m.'.format(juros_total))
