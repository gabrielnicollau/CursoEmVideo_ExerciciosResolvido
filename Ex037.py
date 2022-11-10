# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Ler um número inteiro.

número = int(input('Digite um número inteiro: '))

# Opção de escolha da base de conversão.
# 1 — para binário.
# 2 — para octal.
# 3 — para hexadecimal.
print('''Escolha uma das bases para conversão:')
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL.''')

# Escolha da base

escolha = int(input('Sua opção: '))

# Para binário
if escolha == 1:
    binário = bin(número)
    print('O valor convertido de decimal para BINÁRIO é igual a {}'.format(binário[2::]))
    # 2:: pular os 2 primeiros elementos.

# Para octal.
elif escolha == 2:
    octal = oct(número)
    print('O valor convertido de decimal para octal é igual a {}'.format(octal[2::]))
    # 2:: pular os 2 primeiros elementos.

# Para hexadecimal.
elif escolha == 3:
    hexadecimal = hex(número)
    print('O valor convertido de decimal para hexadecimal é igual a {}'.format(hexadecimal[2::]))
    # 2:: pular os 2 primeiros elementos.

else:
    print('\033[31mVocê digitou uma opção inválida.\033[m')
