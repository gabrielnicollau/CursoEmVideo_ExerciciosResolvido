"""
Exercício Python 57: faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
errado, peça a digitação novamente até ter um valor correto.
"""

sexo = input('Informe seu sexo [M/F]: ').upper().strip()[0]  # [0] --> Pegar a primeira letra digitada.
print('=-' * 16)
while sexo != 'M' and sexo != 'F':  # Podemos fazer também while sexo not in 'MmFf'.
    # Caso não tem MmFf digitado em sexo, vai mandar perguntar denovo.
    sexo = input('Digite um sexo válido [M/F]: ').upper().strip()[0]  # [0] --> Pegar a primeira letra digitada.
    print('=-' * 16)
print('Sexo {} registrado!'.format(sexo))
