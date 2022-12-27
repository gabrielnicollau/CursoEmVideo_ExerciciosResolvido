"""Exercício Python 61: refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while."""


print('=-' * 17)
print('\033[33mOS 10 PRIMEIROS TERMOS DE UMA PA\033[m')
print('=-' * 17)

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))

mais = 10  # Limite de 10 termos.
total = 0  # Variável para fazer a soma de termos.
cont = 1  # Contar a quantidade de loop's.

while mais != 0:  # Enquanto mais não receber o input com valor 0, vai ficar em loop perguntado qual o valor.
    total = total + mais

    while cont <= total:  # Cont sempre vai ser menor que total(total vale 10), vai ficar em loop até 'mais' receber zero., cont vai ficar maior.
        print('\033[32m{}\033[m \033[34m--> \033[m'.format(termo), end='')
        cont += 1  # Vai contar +1 para cada loop.
        termo += razão  # razão vai ser somado ao termo em cada loop, ou seja, termo = termo(variável) + razão (valor fixo).
    print('\033[33mPAUSA...\033[m')
    mais = int(input('MAis quantos termos você gostaria de ver ? '))
print('\033[33mFIM!\033[m')
