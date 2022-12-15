"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))

escolha = 0
while escolha != 5:  # while != 5, qual número digitado iria servir e iria ficar no loop (verdadeiro), quando
    # fosse igual a 5 iria virar falso e iria sair do loop encerrar.
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    escolha = int(input('   > Qual é a sua opção ? '))

    if escolha == 1:
        soma = valor_1 + valor_2
        print('     A soma de {} + {} = {}'.format(valor_1, valor_2, soma))
        print('=-' * 25)

    elif escolha == 2:
        multiplicador = valor_1 * valor_2
        print('     O resultado de {} x {} = {}'.format(valor_1, valor_2, multiplicador))

    elif escolha == 3:
        if valor_1 > valor_2:
            maior = valor_1
            print('Entre {} e {} o maior valor é {}'.format(valor_1, valor_2, maior))

        else:
            maior = valor_2
            print('Entre {} e {} o maior valor é {}'.format(valor_1, valor_2, maior))

    elif escolha == 4:
        print('NOVOS VALORES...')
        valor_1 = int(input('Digite o primeiro valor: '))
        valor_2 = int(input('Digite o segundo valor: '))

    elif escolha == 5:
        print('Finalizando...')
