print('Bem vindo ao Programa de Feijoada do Thiago Antunes Pereira de Lima') # Identificador pessoal.


def volumeFeijoada(): # Função de escolha da quantidade da feijoada.

    while True:

        print('Menu Volume Feijoda')
        try:
            volumeFeijoada = float(input('Entre com a quantidade desejada(ml):')) # Volume da feijoada.
        except ValueError:
            print("Valor não numérico!")
            continue

        if volumeFeijoada <= 299 or volumeFeijoada >= 5001: # Limitador do volume.
            print('Não aceitamos porções menores de 300 ml ou maiores de 5 L. Tente Novamente!')
            continue
        else:
            return volumeFeijoada * 0.08


def opcaoFeijoada():  # Função do tamanho da feijoada.
    while True:
        opcaoFeijoada = input('Menu Opção Feijoada\n'       # Escolha do multiplicador.
                              'B - Básica - (Feijão + Paiol + Costelinha)\n'
                              'P - Premium - (Feijão + Paiol + Costelinha + Partes de Porco)\n'
                              'S - Suprema - (Feijão + Paiol + Costelinha + Partes de Porco + Charge + Calabresa + Bacon)\n'
                              'Entre com a opção da feijoada:\n'
                              '>>')

        if opcaoFeijoada.upper() == 'B':
            subtotal2 = 1
            return subtotal2

        elif opcaoFeijoada.upper() == 'P':
            subtotal2 = 1.25
            return subtotal2

        elif opcaoFeijoada.upper() == 'S':
            subtotal2 = 1.5
            return subtotal2

        else:
            print('Digite uma opção válida')
            continue


def acompanhamentoFeijoada(): # Função com opções de acompanhamento.
    total = 0
    contador = 0
    while True:
        adicional = input('Deseja mais algum acompanhamento?\n'
                              '0- Não desejo mais acompanhamentos (encerrar pedido)\n'
                              '1- 200g de arroz	5,00\n'
                              '2- 150g de farofa especial	6,00\n'
                              '3- 100g de couve cozida	7,00\n'
                              '4- 1 laranja descascada	3,00\n'
                              '>>')

        if adicional == '1':
            subtotal3 = 5
            contador += subtotal3
            total = total + subtotal3
            continue

        elif adicional == '2':
            subtotal3 = 6
            contador += subtotal3
            total = total + subtotal3
            continue

        elif adicional == '3':
            subtotal3 = 7
            contador += subtotal3
            total = total + subtotal3
            continue

        elif adicional == '4':
            subtotal3 = 3
            contador += subtotal3
            total = total + subtotal3
            continue

        elif adicional == '0':
            subtotal3 = 0
            total = total + subtotal3
            return total

        else:
            print('digite um codigo de acompanhento!')
            continue


#Programa Principal:

x = volumeFeijoada()
y = opcaoFeijoada()
z = acompanhamentoFeijoada()
total = x*y+z

print('O valor a ser pago é de R${}(volume = {} * opção = {} + acompanhemto = {})'.format(total, x, y, z))
#Fim do Programa