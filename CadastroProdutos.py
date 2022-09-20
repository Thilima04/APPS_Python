listaProdutos = []  # Lista dos produtos.


def cadastrarProduto(codigo): # Função de cadastrar produto.

    print('Você escolheu a opção de cadastrar produto.')
    print('Código do Produto {}'.format(codigo))
    nome = input('Por favor entre com o NOME do produto:')
    fabricante = input('Por favor entre com o FABRICANTE do produto:')
    valor = float(input('Por favor entre com o VALOR(R$) do produto:'))
    dicionarioProduto = {'Código': codigo,                            # Criação do dicionário
                         'Nome': nome,
                         'Fabricante': fabricante,
                         'Valor': valor}
    listaProdutos.append(dicionarioProduto.copy())     #Passagem dos valores para a lista.


def consultarProduto(): #Função para consultar os produtos
    while True:
        try:  # Validação para digitar as opções corretas do menu.
            opconsul = int(input('Você selecionou a opção Consultar Protudo\n'
                                 '1 - Consultar todos os produtos\n'
                                 '2 - Consultar produtos por código\n'
                                 '3 - Consultar produtos por fabricante\n'
                                 '4 - Retornar\n'
                                 '>>'))
            if opconsul == 1: # Opção de consultar todos os produtos.
                for produto in listaProdutos:
                    for key, value in produto.items():
                        print('{}:{}'.format(key, value))

            elif opconsul == 2: # Opção de consultar produto por código.
                consulcod = int(input('Digite o número do código:\n'
                                      '>>'))
                for produto in listaProdutos:
                    if produto['Código'] == consulcod:
                        for key, value in produto.items():
                            print('{}:{}'.format(key, value))

            elif opconsul == 3: # Opção de consultar produto por fabricante.
                consulfabr = input('Digite o nome do fabricante:\n'
                                   '>>')
                for produto in listaProdutos:
                    if produto['Fabricante'] == consulfabr:
                        for key, value in produto.items():
                            print('{}:{}'.format(key, value))

            elif opconsul == 4: # Opção de voltar para o menu principal.
                break

        except ValueError:
            print('Pare de digitar numeros não inteiros!')


def removerProduto(): # Função de remover produtos.
    print('Você selecionou a opção de remover produto.')

    remover = int(input('Digite o código do produto a ser removido:\n' # Código do produto a ser removido.
                        '>>'))

    for produto in listaProdutos:
        if produto['Código'] == remover:
           listaProdutos.remove(produto)


#Programa Principal
print('Bem Vindo ao Controle de Estoque da Mercearia do Thiago Antunes Pereira de Lima') # Identificador pessoal

codigo = 0 # Contador iniciando em zero.

while True:
    try: # Validação das opções do menu.

        op = int(input('Escolha a opção desejada:\n' # Menu Principal
                       '1 - Cadastrar Produto\n'
                       '2 - Consultar Produto(s)\n'
                       '3 - Remover Produto\n'
                       '4 - Sair\n'
                       '>>'))

        if op == 1:
            codigo = codigo + 1
            cadastrarProduto(codigo)
        elif op == 2:
            consultarProduto()
        elif op == 3:
            removerProduto()
        elif op == 4:
            print('Você escolheu a opção sair.\n'
                  'Desligando programa!')
            break # Fim do programa.

    except ValueError:
        print('Pare de digitar numeros não inteiros!')
        continue
