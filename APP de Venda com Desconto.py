print('Bem vindo ao APP de Venda do Thiago Antunes Pereira de Lima') # Identificador pessoal

# Entrada dos valores para calculo.
valor_p = float(input('Entre com o valor do produto:'))  # Recebe o valor do produto.

quant = int(input('Entre com a quantidade:'))  # Recebe a quantidade do produto.

valor_t = valor_p * quant

# Calculo sem desconto.
if quant <= 4:
    print('O valor é de:R${}'.format(valor_t))

# Calculos com desconto.
elif quant <= 19:
    valor_d = valor_t - (valor_t * 0.03)
    print('O valor sem desconto é de:R${}'.format(valor_t))
    print('O valor com desconto é de:R${} (Desconto de 3%)'.format(valor_d))

elif quant <= 99:
    valor_d = valor_t - (valor_t * 0.06)
    print('O valor sem desconto é de:R${}'.format(valor_t))
    print('O valor com desconto é de:R${} (Desconto de 6%)'.format(valor_d))

else:
    valor_d = valor_t - (valor_t * 0.10)
    print('O valor sem desconto é de:R${}'.format(valor_t))
    print('O valor com desconto é de:R${} (Desconto de 10%)'.format(valor_d))
