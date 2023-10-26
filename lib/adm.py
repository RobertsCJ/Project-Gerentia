import os
import sqlite3
import secrets
import pwinput
from os import system
from time import sleep


def limpar_a_tela() -> None:
    """
    Limpa a tela do terminal.
    :return:
    """
    system('cls' if os.name == 'nt' else 'clear')


def criar_tabela_funcionarios(cursor):
    """
    Cria uma tabela de funcionários se ela não existir.
    :param cursor: Cursor do banco de dados SQLite.
    :return:
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
        matricula NOT NULL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cargo VARCHAR(100),
        nome_usuario VARCHAR(100),
        senha VARCHAR(25)
        );
    """)


def cadastrar_funcionario(cursor):
    """
    Cadastra um novo funcionário na tabela de funcionários.
    :param cursor: Cursor do banco de dados SQLite.
    :return:
    """
    limpar_a_tela()
    criar_tabela_funcionarios(cursor)
    matricula = secrets.token_hex(5)
    nome = str(input('Nome do funcionário: '))
    cargo = str(input('Cargo do funcionário? '))
    nome_usuario = str(input('Nome de usuário: '))
    senha = pwinput.pwinput('Cadastre uma senha: ')
    cursor.execute("""
    INSERT INTO funcionarios (matricula, nome, cargo, nome_usuario, senha)
    VALUES(?, ?, ?, ?, ?);
    """, (matricula, nome, cargo, nome_usuario, senha))


def demitir_funcionario(cursor):
    """
    Demite um funcionário da tabela de funcionários.
    :param cursor: Cursor do banco de dados SQLite.
    :return:
    """
    limpar_a_tela()
    print(f'{"-" * 100}\n{"REMOVENDO FUNCIONÁRIO":^100}\n{"-" * 100}')
    matricula = str(input('Informe a matricula do funcionário: '))
    cursor.execute("""
    DELETE FROM funcionarios WHERE matricula = ?;
    """, (matricula,))
    print(f'{"-" * 100}\n{"FUNCIONÁRIO DEMITIDO":^100}\n{"-" * 100}')


def alterar_dados(cursor):
    """
    Altera os dados de um funcionário na tabela de funcionários.
    :param cursor: Cursor do banco de dados SQLite.
    :return:
    """
    print(f'{"-"*160}\n{"ATUALIZAÇÃO CADASTRAL":^160}\n{"-"*160}')
    mostrar_funcionarios(cursor)
    matricula = str(input('Informe a matricula do funcionário: '))
    novo_cargo = str(input('Qual será o novo cargo do funcionário? '))
    cursor.execute("""
    UPDATE funcionarios SET cargo = ? WHERE matricula = ?;
    """, (novo_cargo, matricula))
    print(f'{"-"*160}\n{"ATUALIZADO COM SUCESSO!":^160}\n{"-"*160}')


def mostrar_funcionarios(cursor):
    """
    Mostra os dados dos funcionários na tabela de funcionários.
    :param cursor: Cursor do banco de dados SQLite.
    :return:
    """
    cursor.execute("""
   SELECT * FROM funcionarios;
   """)
    dados = cursor.fetchall()

    print(f'{"-" * 100}\n{"FUNCIONÁRIOS CADASTRADOS":^100}\n{"-" * 100}')
    print(f'{"MATRICULA":10} | {"NOME":25} | {"CARGO":25} | {"NOME USUÁRIO":15} | {"SENHA"}\n{"-" * 100}')
    for dado in dados:
        print(f'{dado[0]:^10} | {dado[1]:25} | {dado[2]:25} | {dado[3]:15} | {dado[4]}')


def ver_vendas_de_um_dia(cursor) -> None:
    """
    Solicita ao usuário que insira um dia, mês e ano. Em seguida, recupera todos os registros da tabela 'vendas'
    que têm a data especificada e os imprime.
    :param cursor:
    :return:
    """
    total = 0
    dia = input('Digite o dia: ')
    mes = input('Digite o mês: ')
    ano = input('Digite o ano: ')
    data = f'{ano}-{mes}-{dia}'

    cursor.execute("""
    SELECT * FROM vendas WHERE data = ?;
    """, (data,))
    vendas = cursor.fetchall()

    print(f'{"-"*160}\n{"VENDAS DO DIA":^160}\n{"-"*160}')
    print(f'{"ID":4} | {"NOME":20} | {"QUANTIDADE":10} | {"VALOR":5} | {"TOTAL":5} | {"DATA":10} | {"HORA"}')
    print(f'{"-"*160}')
    for venda in vendas:
        print(f'{venda[0]:4} | {venda[1]:20} | {venda[2]:10} | {venda[3]:5} | {venda[4]:5} | {venda[5]:10} | {venda[6]}')
        total += venda[4]
    print(f'O total vendido R${total:.2f}')


def ver_vendas(cursor) -> None:
    """
    Recupera todos os registros da tabela 'vendas' e os imprime.
    :param cursor:
    :return:
    """
    total = 0
    cursor.execute("""
    SELECT * FROM vendas;
    """)
    vendas = cursor.fetchall()

    print(f'{"-"*160}\n{"VENDAS REALIZADAS":^160}\n{"-"*160}')
    print(f'{"ID":4} | {"NOME":20} | {"QUANTIDADE":10} | {"VALOR":5} | {"TOTAL":5} | {"DATA":10} | {"HORA"}')
    print(f'{"-"*160}')
    for venda in vendas:
        print(f'{venda[0]:4} | {venda[1]:20} | {venda[2]:10} | {venda[3]:5} | {venda[4]:5} | {venda[5]:10} | {venda[6]}')
        total += venda[4]
    print(f'O total vendido R${total:.2f}')


def menu():
    print(f"""{"-"*160}\n{"MENU":^160}\n{"-"*160}
1 - CADASTRAR FUNCIONÁRIO 
2 - ATUALIZAR CADASTRO
3 - VER FUNCIONÁRIOS
4 - DEMITIR FUNÁRIOS
5 - SAIR\n{"-"*160}
    """)


def sistema_adm():
    conn = sqlite3.connect('database/gerentia.db')
    cursor = conn.cursor()
    continuar = True
    while continuar:
        menu()
        opcao = int(input('Escolha a opção desejada: '))

        if opcao == 1:
            cadastrar_funcionario(cursor)
        elif opcao == 2:
            alterar_dados(cursor)
        elif opcao == 3:
            mostrar_funcionarios(cursor)
        elif opcao == 4:
            demitir_funcionario(cursor)
        elif opcao == 5:
            continuar = False
        else:
            print('ERRO! Opção inválida.')

        conn.commit()
    conn.close()
    limpar_a_tela()

    print('ENCERRANDO PROGRAMA.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    limpar_a_tela()
    print(f'{"-"*160}\n{"PROGRAMA ENCERRADO"}\n{"-"*160}')
