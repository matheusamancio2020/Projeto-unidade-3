import random
from style import *

usuarios = {1: {'nome': 'matheus', 'senha': '1234567', 'tipo': 'adm'}}
admin_password = "1234567"


def admin_menu():
    espacamento()
    print(verde('Usuário logado como administrador \u2714'))
    print(azul('[1] Adicionar filmes \u002B'))
    print(azul('[2] Buscar filmes \U0001F50D'))
    print(azul('[3] Atualizar filmes \u21BB'))
    print(azul('[4] Remover filmes X'))
    print(azul('[5] Visualizar ingressos vendidos'))
    print(azul('[6] Visualizar ingressos vendidos por filme'))
    print(azul('[7] Gerar relatório de ingressos vendidos'))
    print(azul('[8] Gerar gráfico sobre a venda de filmes'))
    print(azul('[9] Visualizar a receita total da venda de ingressos'))
    print(azul('[10] Sair do perfil'))
    espacamento()


def mostrar_menu_usuario():
    print(azul('[1] Visualizar filmes disponíveis'))
    print(azul('[2] Compra de ingressos'))
    print(azul('[3] Buscar filme'))
    print(azul('[4] Listar ingressos comprados'))
    print(azul('[5] Gerar arquivo TXT com ingressos comprados'))
    print(azul('[6] Visualizar filmes mais populares'))
    print(azul('[7] Sair do perfil'))
    espacamento()


def cadastrar_usuario():
    tipo_usuario = input(
        roxo('Você deseja cadastrar um administrador ou um usuário comum? (adm/comum): ')).lower()
    if tipo_usuario not in ['adm', 'comum']:
        print(vermelho('Opção inválida. Por favor, escolha "adm" ou "comum".'))
        return

    if tipo_usuario == 'adm':
        admin_senha = input(roxo('Digite a senha de administrador para realizar o cadastro: '))
        if admin_senha != admin_password:
            print(vermelho('Senha de administrador incorreta. Cadastro não autorizado.'))
            return

    cadastrousuario = input(roxo('Digite o seu nome, usuário: '))
    if not cadastrousuario.isalpha() or len(cadastrousuario) < 6:
        print(vermelho('O nome do usuário precisa ter pelo menos 6 caracteres e ser composto apenas por letras'))
        return

    senhausuario = input(roxo('Digite sua senha: '))
    if not senhausuario.isnumeric() or len(senhausuario) < 6:
        print(vermelho('A senha precisa ter pelo menos 6 dígitos e ser composta apenas por números'))
        return

    idusuario = random.randint(3, 1000)
    while idusuario in usuarios:
        idusuario = random.randint(3, 1000)

    usuarios[idusuario] = {'nome': cadastrousuario, 'senha': senhausuario,
                           'tipo': 'adm' if tipo_usuario == 'adm' else 'usuariocomum'}
    print(verde('Usuário cadastrado com sucesso \u2714'))


def menu_principal():
    espacamento()
    print(verde(negrito('CINE SERTÃO 🌵')))
    espacamento()
    print(sublinhado(azul('MENU')))
    print(azul('[1] Login: ' + '\n' + '[2] Cadastrar usuário: ' + '\n' + '[3] Sair'))
    espacamento()


def login(usuario, senha):
    for user in usuarios.values():
        if user['nome'] == usuario and user['senha'] == senha:
            return user
    return None



