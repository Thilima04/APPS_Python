print('Programa de Vendas para Pizzarias de Thiago Antunes Pereira de Lima') # Identificador pessoal

print('=====================Cardápio do dia=====================') #Cardápio

print('| Código | | Descrição | | Pizza Média | | Pizza Grande |')

print('|   21   | |Napolitana | |   R$20,00   | |    R$26,00   |')

print('|   22   | |Margherita | |   R$20,00   | |    R$26,00   |')

print('|   23   | |Calabresa  | |   R$25,00   | |    R$32,50   |')

print('|   24   | |Toscana    | |   R$30,00   | |    R$39,00   |')

print('|   25   | |Portuguesa | |   R$30,00   | |    R$39,00   |')

print('=========================================================')

contador = 0     #Quantidade de pizzas compradas.
total = 0        #Valor total a pagar.

while True:

    tam = input('Qual o tamanho da Pizza?(M ou G)') # Escolha do tamanho.

    if tam.upper() == 'M':
        subtotal = 1
    elif tam.upper() == 'G':
        subtotal = 1.3
    else:
        print('Opção Invalida!')
        continue


    pizza = int(input('Qual o codigo da pizza?\n'  # Escolha do sabor da pizza.
                      'Digite o código:'))

    if pizza == 21 or pizza == 22:
        valor = 20 * subtotal
    elif pizza == 23:
        valor = 25 * subtotal
    elif pizza == 24 or pizza == 25:
        valor = 30 * subtotal
    else:
        print('Opção Invalida')
        continue

    contador += 1
    total = total + valor
    resp = input('Deseja pedir algo mais?(S/N)')   #Opção de compra de mais itens.

    if resp.upper() == 'S':
        continue

    print('O total a ser pago é de R$ {}'.format(total))

    break   #Fim do programa.