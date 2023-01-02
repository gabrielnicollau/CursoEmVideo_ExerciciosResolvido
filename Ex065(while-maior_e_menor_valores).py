"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

escolha = 'S'  # Escolha sim.
soma_num = 0  # Soma começa com zero.
quant_num = 0  # Quantidade começa com zero.
lista = []  # Lista vazia

while escolha == 'S':  # Enquanto o usuário digitar 'S'.
    numeros = int(input('Digite um valor: '))  # Vai perguntar o número.
    escolha = str(input('Quer continuar [S/N] ? ')).title().strip()[0]  # Caso a resposta seja 'S', vai perguntar o número novamente.

    lista.append(numeros)  # Vai pegar os números e jogar na lista com append.
    soma_num = soma_num + numeros  # soma os valores de número.
    quant_num = quant_num + 1  # quantos vezes foi digitado os números

media = soma_num / quant_num  # Média dos números, não precisa está no loop, visto que já tem os valores guardados.


print('Foram digitados {} números. A soma desses números foi {} e a média é {:.1f}.'.format(quant_num, soma_num, media))
print('O menor valor foi {} e o maior foi {}.'.format(min(lista), max(lista)))
