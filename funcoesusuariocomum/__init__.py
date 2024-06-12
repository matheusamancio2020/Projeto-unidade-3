from funcoesdoadm import *

compras_por_cliente = {}


def visualizar_filmes():
    print(azul("Filmes Disponíveis:"))
    for filme in dados:
        print(f"Título: {filme['Titulo']}\nHorário: {filme['Horario']}\nData: {filme['Data']}\nPreço: {filme['Preço']}\nSinopse: {filme['Sinopse']}")


def compra_ingressos(usuario):
    titulo_filme = input(azul("Digite o título do filme que deseja comprar ingresso: "))
    for filme in dados:
        if titulo_filme.lower() == filme['Titulo'].lower():
            quantidade_disponivel = filme['Quantidade Ingressos']
            print(azul(f"Quantidade de ingressos disponíveis para {titulo_filme}: {quantidade_disponivel}"))
            while True:
                qtd_ingressos = input(azul("Digite a quantidade de ingressos desejados: "))
                if qtd_ingressos.isdigit():
                    qtd_ingressos = int(qtd_ingressos)
                    if qtd_ingressos <= quantidade_disponivel:
                        print(verde(f"Ingressos comprados com sucesso para {titulo_filme}!"))
                        filme['Quantidade Ingressos'] -= qtd_ingressos
                        if usuario not in compras_por_cliente:
                            compras_por_cliente[usuario] = []
                        compras_por_cliente[usuario].append({'filme': titulo_filme, 'quantidade': qtd_ingressos})
                        vendas.append({'cliente': usuario, 'filme': titulo_filme, 'quantidade': qtd_ingressos})
                        break
                    else:
                        print(vermelho("Quantidade de ingressos desejados não está disponível. Tente novamente."))
                else:
                    print(vermelho("Por favor, insira um número válido."))
            break
    else:
        print(vermelho("Filme não encontrado. Por favor, verifique o título digitado."))


def buscar_filme_usuario():
    busca = input(azul('Qual filme deseja realizar a busca?: '))
    for filme in dados:
        if busca.lower() in filme['Titulo'].lower():
            print(f"Título: {filme['Titulo']}\nHorário: {filme['Horario']}\nData: {filme['Data']}\nPreço: {filme['Preço']}\nSinopse: {filme['Sinopse']}")


def listar_ingressos_comprados_cliente(usuario):
    if usuario in compras_por_cliente:
        print(azul(f"Ingressos comprados por {usuario}:"))
        for compra in compras_por_cliente[usuario]:
            print(f"Filme: {compra['filme']}, Quantidade: {compra['quantidade']}")
    else:
        print(vermelho("Nenhum ingresso comprado ainda."))


def visualizar_filmes_populares():
    filmes_ordenados = []
    for filme in dados:
        inserido = False
        for i, f in enumerate(filmes_ordenados):
            if filme['Quantidade Ingressos'] > f['Quantidade Ingressos']:
                filmes_ordenados.insert(i, filme)
                inserido = True
                break
        if not inserido:
            filmes_ordenados.append(filme)

    print(azul("Filmes mais populares: "))
    for filme in filmes_ordenados:
        print(f"Título: {filme['Titulo']}, Ingressos Disponíveis: {filme['Quantidade Ingressos']}")


def gerar_arquivo_ingressos_cliente(usuario):
    with open(f'{usuario}_ingressos_comprados.txt', 'w') as arquivo:
        arquivo.write(f"Ingressos comprados por {usuario}:\n")
        if usuario in compras_por_cliente:
            for compra in compras_por_cliente[usuario]:
                arquivo.write(f"Filme: {compra['filme']}, Quantidade: {compra['quantidade']}\n")
        else:
            arquivo.write("Nenhum ingresso comprado ainda.\n")
    print(verde(f"Arquivo {usuario}_ingressos_comprados.txt gerado com sucesso."))




