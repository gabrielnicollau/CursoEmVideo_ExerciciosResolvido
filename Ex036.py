# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

# Variável para input valor da casa, salário do comprador e quantos anos ele vai pagar.

casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o valor do seu salário ? '))
anos = int(input('Em quantos anos pretende pagar ? '))

# Calculo de prestação.

# Prestação é mensal.
prestação = casa / (anos * 12)  # Cálculo para descobrir quanto vai pagar por mês.

# valor mínimo que não pode exceder 30% do salário.

mínimo = salario * 30 / 100  # 30% do salário.

# Condição da compra.

print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f} reais'.format(casa, anos, prestação))

if prestação <= mínimo:  # O valor da prestação tem que ser menor que 30% do salário.
    print('Empréstimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print(' Empréstimo \033[31mNegado!\033[m')
