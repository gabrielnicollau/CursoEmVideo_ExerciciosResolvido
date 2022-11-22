# Exercício Python 42: refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que categoria de triângulo
# será formado:
#
# — EQUILÁTERO: todos os lados iguais.
#
# – ISÓSCELES: dois lados iguais, um diferente.
#
# – ESCALENO: todos os lados diferentes.

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

# Verificar se vai formar um triângulo.
# Se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
if reta3 + reta2 > reta1 and reta3 + reta1 > reta2 and reta1 + reta2 > reta3:
    print('\033[32mÉ POSSÍVEL formar um TRIÂNGULO: \033[M', end='')

    if reta1 == reta2 == reta3:  # EQUILÁTERO: todos os lados iguais.
        print('EQUILÁTERO!')

    elif reta1 != reta2 != reta3 != reta1:  # ISÓSCELES: dois lados iguais, um diferente.
        print('ESCALENO!')

    else:  # ISÓSCELES: dois lados iguais, um diferente.
        print('ISÓSCELES!')

else:
    print('\033[31mNão é possível formar um TRIÂNGULO!\033[m')
