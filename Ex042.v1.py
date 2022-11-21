# Exercício Python 035: desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

# leia o comprimento de três retas
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

# "se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo"

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('\033[32mÉ POSSÍVEL\033[m formar UM TRIÂNGULO com essas medidas.')

else:
    print('\033[31mNÃO É POSSÍVEL\033[m formar UM TRIÂNGULO com essas medidas.')
