from style import *
import matplotlib.pyplot as plt
from usuarios import *

usuarios = {1: {'nome': 'matheus', 'senha': '1234567', 'tipo': 'adm'}}
filme_sinopse = """Após dois anos espreitando as ruas como Batman, Bruce Wayne se encontra 
nas profundezas mais sombrias de Gotham City. Com poucos aliados confiáveis, 
o vigilante solitário se estabelece como a personificação da vingança para a população."""
filmes = {"Titulo": "Batman", "Horario": "18:30", "Data": "01/01/2025", "Preço": "15 ", "Quantidade Ingressos": 100, "Sinopse": filme_sinopse}
dados = [filmes]
vendas = []



def adicionar_filmes():
    while True:
        quantfilm = input(azul('Quantos filmes deseja adicionar: '))

        if quantfilm.isdigit():
            quantfilm = int(quantfilm)
            for c in range(quantfilm):
                filme = {}
                filme['Titulo'] = input(azul('Adicione o título: '))
                filme['Horario'] = input(azul('Adicione horário (HH:MM): '))
                filme['Data'] = input(azul('Adicione a data (DD/MM/AAAA): '))

                while True:
                    preco = input(azul('Adicione o novo preço: '))
                    if preco.isdigit():
                        filme['Preço'] = int(preco)
                        break
                    else:
                        print(vermelho('Preço inválido. Por favor, insira um número inteiro.'))


                while True:
                    ingressos = input(azul('Adicione a quantidade de ingressos disponíveis: '))
                    if ingressos.isdigit():
                        filme['Quantidade Ingressos'] = int(ingressos)
                        break
                    else:
                        print(vermelho('Por favor, insira apenas números para a quantidade de ingressos disponíveis.'))



                filme['Sinopse'] = input(azul('Adicione a sinopse: '))
                dados.append(filme)
            print(verde('Filme(s) adicionado(s) com sucesso.'))
            break
        else:
            print(vermelho('Por favor, insira apenas números para a quantidade de filmes a ser digitada.'))


def atualizar_filmes():
    escolhaadm = input(azul('Qual filme deseja atualizar?: '))
    filme_encontrado = False
    for filme in dados:
        if escolhaadm.lower() == filme['Titulo'].lower():
            print(azul('Filme encontrado!'))
            filme['Titulo'] = input(azul('Adicione o novo título: '))
            filme['Horario'] = input(azul('Adicione o novo horário: '))
            filme['Data'] = input(azul('Adicione a nova data: '))

            while True:
                preco = input(azul('Adicione o novo preço: '))
                if preco.isdigit():
                    filme['Preço'] = int(preco)
                    break
                else:
                    print(vermelho('Preço inválido. Por favor, insira um número inteiro.'))

            while True:
                quantidade_ingressos = input(azul('Adicione a nova quantidade de ingressos disponíveis: '))
                if quantidade_ingressos.isdigit():
                    filme['Quantidade Ingressos'] = int(quantidade_ingressos)
                    break
                else:
                    print(vermelho('Quantidade inválida. Por favor, insira um número inteiro.'))

            filme['Sinopse'] = input(azul('Adicione a nova sinopse: '))
            print(verde('Filme atualizado com sucesso!'))
            filme_encontrado = True
            break
    if not filme_encontrado:
        print(vermelho('Filme não encontrado. Por favor, verifique o título digitado.'))


def remover_filmes():
    print(azul("Lista de Filmes:"))
    for filme in dados:
        espacamento()
        for chave, valor in filme.items():
            print(f"{chave}: {valor}")
        espacamento()
    escolhaadm = input(azul('Qual filme deseja remover: '))
    for filme in dados:
        if escolhaadm.lower() == filme['Titulo'].lower():
            dados.remove(filme)
            print(verde('Filme removido com sucesso!'))
            break


def listar_ingressos_vendidos_por_filme():
    titulo_filme = input(azul('Digite o título do filme: '))
    print(azul(f"Ingressos vendidos para {titulo_filme}:"))

    ingressos_vendidos = False

    for venda in vendas:
        if venda['filme'].lower() == titulo_filme.lower():
            print(f"Cliente: {venda['cliente']}, Quantidade: {venda['quantidade']}")
            ingressos_vendidos = True

    if not ingressos_vendidos:
        print(azul('Nenhum ingresso foi vendido para este filme.'))


def gerar_arquivo_ingressos_vendidos():
    titulo_filme = input(azul('Digite o título do filme: '))
    with open(f'{titulo_filme}_ingressos_vendidos.txt', 'w') as arquivo:
        arquivo.write(f"Ingressos vendidos para {titulo_filme}:\n")
        for venda in vendas:
            if venda['filme'].lower() == titulo_filme.lower():
                arquivo.write(f"Cliente: {venda['cliente']}, Quantidade: {venda['quantidade']}\n")
    print(verde(f"Arquivo {titulo_filme}_ingressos_vendidos.txt gerado com sucesso."))


def listar_ingressos_vendidos():
    if not vendas:
        print(azul("Nenhum ingresso foi vendido."))
    else:
        print(azul("Ingressos vendidos:"))
        for venda in vendas:
            print(f"Cliente: {venda['cliente']}, Filme: {venda['filme']}, Quantidade: {venda['quantidade']}")



def buscar_filmes():
    busca = input(azul('Qual filme deseja realizar a busca?: '))
    filme_encontrado = False
    for filme in dados:
        if busca.lower() in filme['Titulo'].lower():
            filme_encontrado = True
            print(f"Filme encontrado:\nTítulo: {filme['Titulo']}\nHorário: {filme['Horario']}\nData: {filme['Data']}\nPreço: {filme['Preço']}\nQuantidade Ingressos: {filme['Quantidade Ingressos']}\nSinopse: {filme['Sinopse']}")
    if not filme_encontrado:
        print(vermelho('Filme não encontrado. Por favor, verifique o título digitado.'))


def gerar_grafico_ingressos_por_filme():
    ingressos_por_filme = {}
    for venda in vendas:
        filme = venda['filme']
        quantidade = venda['quantidade']
        if filme in ingressos_por_filme:
            ingressos_por_filme[filme] += quantidade
        else:
            ingressos_por_filme[filme] = quantidade

    filmes = list(ingressos_por_filme.keys())
    ingressos = list(ingressos_por_filme.values())

    plt.figure(figsize=(12, 6))
    plt.bar(filmes, ingressos, color='skyblue', edgecolor='black')
    plt.xlabel('Filmes', fontsize=14)
    plt.ylabel('Ingressos Vendidos', fontsize=14)
    plt.title('Ingressos Vendidos por Filme', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def calcular_total_vendas():
    total_vendas = 0
    for venda in vendas:
        for filme in dados:
            if filme['Titulo'].lower() == venda['filme'].lower():
                total_vendas += int(filme['Preço']) * venda['quantidade']
                break
    print(verde(f"O total arrecadado com as vendas de ingressos é: R${total_vendas}"))









