# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

'''dia_da_semana = str(input('Qual é o dia da semana ? '))
if dia_da_semana == 'Domingo' or dia_da_semana == 'Sábado':
    print('Hoje é dia de descanso')

else:
    print('Você precisa trabalhar!')
####################################################################

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

fruta = str(input('Nome da fruta: '))
lista_de_frutas = ['Banana', 'Melancia', 'Morango', 'Acabati']
for buscar in lista_de_frutas:
    if buscar == 'Morango':
        print('Na lista tem Morango.')
    else:
        print('Não tem Morango na lista.')
#########################################################################################################################

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista

# Crie uma tupla com 4 elementos

tupla = (1, 2, 3, 4)

# Guarde o resultado em uma lista

lista = []

# Multiplique cada elemento da tupla por 2
for elementos_tupla in tupla:
    valor_multiplicado = elementos_tupla * 2
    lista.append(valor_multiplicado)
print(lista)

#########################################################################################################################

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for numeros_100_ao_150 in range(100, 151, 2):
    print(numeros_100_ao_150)

#########################################################################################################################

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela

# Criar variavel chamada temperatura e atrivuir o valor de 40

temperatura = 40

# Condição de enquanto for maior que 40, imprimir na tela

while temperatura > 35:  # loop em temperatura, vai ficar mostrando 40 toda hora
    temperatura = temperatura - 1  # temperatura - 1 vai de 40 até 35
    print(temperatura)

#########################################################################################################################

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

# Criar variavel chamada counter com valor 0

contador = 0

# Enquanto counter for menor que 100 imprimir os valores até encontrar o valor 23

while contador < 100:  # Enquanto for menor que 100 vai executar o if
    if contador == 23:  # Verificar o valor se é 23
        break  # Pause o loop
    contador += 1  # Adicona mais 1 no contador
    print(contador)

#########################################################################################################################

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista

# Criar variável lista

lsita = list()

# Criar uma várial com valor 4

varial_valor4 = 4

# Condição

while varial_valor4 <= 20:
    varial_valor4 = varial_valor4 + 2
    lsita.append(varial_valor4)
print(lsita)
print(type(lsita))

#########################################################################################################################

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
lista = list(nums)
print(lista)

#########################################################################################################################


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')'''

#########################################################################################################################

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a
# vantagem de existir.” (Machado de Assis)

from itertools import count
from typing import Counter


frase = '# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir.” (Machado de Assis)'
#contador = frase.count('R' and 'r')
print('A letraA aparece {} vezes na frase.'.format(frase.count('R' and ('r'))))

#print('A letra A aparece {} vezes'.format(contador))
