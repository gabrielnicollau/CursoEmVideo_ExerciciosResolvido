# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, conforme a média atingida:

# – Média abaixo de 5.0: REPROVADO

# — Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

from time import sleep

primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
print('-=' * 25)
média = (primeira_nota + segunda_nota) / 2

print('\033[34mCalculando...\033[m')
sleep(1.70)  # Time para aparecer a resposta.
print('Suas notas foram {:.1f} e {:.1f}, a sua média é {:.1f}.'.format(primeira_nota, segunda_nota, média))

# – Média abaixo de 5.0: REPROVADO
if média <= 5:
    print('Você está \033[31mREPROVADO!\033[m')

# — Média entre 5.0 e 6.9: RECUPERAÇÃO

elif 7 > média >= 5:  # Condição 7 maior que a nota, se for verdadeira a nota tem que ser maior ou igual a 5
    print('Você está de \033[33mRECUPERAÇÃO!\033[m')

# – Média 7.0 ou superior: APROVADO
elif média >= 7:
    print('Você foi \033[31mAPROVADO!\033[m')
