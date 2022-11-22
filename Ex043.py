# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

########################################################################################################################
# \033[m --> Cores no terminal

# ler o peso e a altura de uma pessoa:

peso = float(input('Digite é seu peso (ex: 50.0Kg): '))
altura = float(input('Digite é sua altura (ex: 1.75cm): '))

# Calcule seu Índice de Massa Corporal (IMC)

imc = peso / (altura ** 2)  # ou podemos usar também: imc = peso / (altura * altura)
print('Seu IMC é: \033[4:37m{:.1f}\033[m'.format(imc))
# Verificar a classificação do seu imc:

# IMC abaixo de 18,5: Abaixo do Peso

if imc < 18.5:
    print('Seu imc indica: \033[34mMAGREZA\033[m.')

# Entre 18,5 e 25: Peso Ideal
elif 18.5 <= imc < 25:  # Se o imc estiver entre 18.5 a 25.
    print('PARABÉNS, seu peso está \033[32mNORMAL\033[m.')

# 25 até 30: Sobrepeso

elif 25 <= imc < 30:
    print('De acordo com seu imc, você está com \033[33mSOBREPESO: GRAU I\033m.')

# 30 até 40: Obesidade

elif 30 <= imc < 40:
    print('De acordo com seu imc, você está com \033[35mOBESIDADE: GRAU II\033[m.')

else:
    print('De acordo com seu imc, você está com \33[31mOBESIDADE: GRAU III\033[m.')
