# Matheus Amancio de Oliveira #
# José Victor Faustino Vieira #

from usuarios import *
from funcoesdoadm import *
from style import *
from funcoesusuariocomum import *


while True:
    menu_principal()
    escolha = input(azul('Digite uma opção: '))
    if not escolha.isdigit():
        print(vermelho("Opção inválida. Por favor, insira um número."))
        continue
    escolha = int(escolha)

    if escolha == 1:

        usuario = input(azul('Digite o seu nome, usuário: '))
        senha = input(azul('Digite sua senha, usuário: '))

        user_data = login(usuario, senha)

        if user_data and user_data['tipo'] == 'adm':
            while True:
                admin_menu()
                gerenciamento = input(azul('Escolha uma opção do menu do administrador: '))
                if not gerenciamento.isdigit():
                    print(vermelho('Insira um valor válido'))
                    continue
                gerenciamento = int(gerenciamento)

                if gerenciamento == 1:
                    adicionar_filmes()
                elif gerenciamento == 2:
                    buscar_filmes()
                elif gerenciamento == 3:
                    atualizar_filmes()
                elif gerenciamento == 4:
                    remover_filmes()
                elif gerenciamento == 5:
                    listar_ingressos_vendidos()
                elif gerenciamento == 6:
                    listar_ingressos_vendidos_por_filme()
                elif gerenciamento == 7:
                    gerar_arquivo_ingressos_vendidos()
                elif gerenciamento == 8:
                    gerar_grafico_ingressos_por_filme()
                elif gerenciamento == 9:
                    calcular_total_vendas()
                elif gerenciamento == 10:
                    print(ciano('Saindo do perfil do administrador...'))
                    break
                else:
                    print(vermelho('Insira um valor válido'))
        elif user_data and user_data['tipo'] == 'usuariocomum':
            print(verde(f'Bem-vindo, {user_data["nome"]}!'))
            while True:
                mostrar_menu_usuario()
                escolhausuario = input(azul('Digite a opção desejada: '))
                if escolhausuario.isnumeric():
                    escolhausuario = int(escolhausuario)
                if escolhausuario == 1:
                    visualizar_filmes()
                elif escolhausuario == 2:
                    compra_ingressos(user_data['nome'])
                elif escolhausuario == 3:
                    buscar_filmes()
                elif escolhausuario == 4:
                    listar_ingressos_comprados_cliente(user_data['nome'])
                elif escolhausuario == 5:
                    gerar_arquivo_ingressos_cliente(user_data['nome'])
                elif escolhausuario == 6:
                    visualizar_filmes_populares()
                elif escolhausuario == 7:
                    print('Saindo do perfil de usuário...')
                    break
                else:
                    print(vermelho('Insira um valor válido'))
        else:
            print(vermelho('Usuário ou senha incorretos. Tente novamente.'))
    elif escolha == 2:
        cadastrar_usuario()
    elif escolha == 3:
        print(ciano("Saindo do sistema. Até mais!"))
        break
    else:
        print(vermelho("Opção inválida. Por favor, escolha uma opção válida."))