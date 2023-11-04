import os
import sqlite3
import secrets
from lib.check_module import *
from os import system
from time import sleep
from datetime import datetime

so = 'cls' if os.name == 'nt' else 'clear'

def limpar_a_tela() -> None:
    """
    Limpa a tela do terminal.
    :return: nothing
    """
    exec(f"system('{so}')")


def log(user, action):
            date_now = datetime.now().date()
            time_now = datetime.now().time()
            data = ''

            data += user + '|'
            data += str(date_now.strftime('%A')) + '|'
            data += str(date_now.strftime('%d/%m/%Y')) + '|'
            data += str(time_now)[:8] + '|\n'
            data += '\t-> ' + action + '\n'
            with open("database/log.txt", 'a') as file:
                file.write(data)


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

class Funcionario:
	def __init__(self, matricula, nome, cargo, nome_usuario, senha):
		self.matricula = matricula
		self.nome = nome
		self.cargo = cargo
		self.nome_usuario = usuario
		self.senha = senha
class BD_Funcionarios:
	def __init__(self, cursor):
	self.cursor = cursor

	def cadastrar_funcionario(self):
		"""
		Cadastra um novo funcionário na tabela de funcionários.
		:param self:
		:return: nothing
		"""
		limpar_a_tela()
		criar_tabela_funcionarios(cursor)
		matricula = secrets.token_hex(5) 
		nome = str(input('Nome do funcionário: '))
		cargo = str(input('Cargo do funcionário? '))
		nome_usuario = str(input('Nome de usuário: '))
		senha = password_module('Cadastre uma senha: ')
		funcionario = Funcionario(matricula, nome, cargo, nome_usuario, senha)

		self.cursor.execute("""
	    	INSERT INTO funcionarios (matricula, nome, cargo, nome_usuario, senha)
	    	VALUES(?, ?, ?, ?, ?);
	    	""", (funcionario.matricula, funcionario.nome, funcionario.cargo, funcionario.nome_usuario, funcionario.senha))
		log("user", f'"{funcionario.nome_usuario}" cadastrado no sistema')

	def demitir_funcionario(self):
		"""
		Demite um funcionário da tabela de funcionários.
		:param self:
		:return:
		"""
		limpar_a_tela()
		print(f'{"-" * 100}\n{"REMOVENDO FUNCIONÁRIO":^100}\n{"-" * 100}')
		matricula = str(input('Informe a matricula do funcionário: '))
		self.cursor.execute("""
		DELETE FROM funcionarios WHERE matricula = ?;
		""", (matricula,))
		print(f'{"-" * 100}\n{"FUNCIONÁRIO DEMITIDO":^100}\n{"-" * 100}')
		log("user", 'user foi demitido') #######

	def alterar_dados(self):
		"""
		Altera os dados de um funcionário na tabela de funcionários.
		:param self:
		:return:
		"""
		print(f'{"-"*160}\n{"ATUALIZAÇÃO CADASTRAL":^160}\n{"-"*160}')
		mostrar_funcionarios(self.cursor)
		matricula = str(input('Informe a matricula do funcionário: '))
		novo_cargo = str(input('Qual será o novo cargo do funcionário? '))
		self.cursor.execute("""
		UPDATE funcionarios SET cargo = ? WHERE matricula = ?;
		""", (novo_cargo, matricula))
		print(f'{"-"*160}\n{"ATUALIZADO COM SUCESSO!":^160}\n{"-"*160}')
		log("user", 'Dado Y  alterado') ##########

	def mostrar_funcionarios(self):
		"""
		Mostra os dados dos funcionários na tabela de funcionários.
		:param self:
		:return:
		"""
		self.cursor.execute("""
		SELECT * FROM funcionarios;
		""")
		dados = self.cursor.fetchall()

		print(f'{"-" * 100}\n{"FUNCIONÁRIOS CADASTRADOS":^100}\n{"-" * 100}')
		print(f'{"MATRICULA":10} | {"NOME":25} | {"CARGO":25} | {"NOME USUÁRIO":15} | {"SENHA"}\n{"-" * 100}')
		for dado in dados:
			print(f'{dado[0]:^10} | {dado[1]:25} | {dado[2]:25} | {dado[3]:15} | {dado[4]}')


	def ver_vendas_de_um_dia(self) -> None:
	    """
	    Solicita ao usuário que insira um dia, mês e ano. Em seguida, recupera todos os registros da tabela 'vendas'
	    que têm a data especificada e os imprime.
	    :param self:
	    :return:
	    """
	    total = 0
	    dia = input('Digite o dia: ')
	    mes = input('Digite o mês: ')
	    ano = input('Digite o ano: ')
	    data = f'{ano}-{mes}-{dia}'

	    self.cursor.execute("""
	    SELECT * FROM vendas WHERE data = ?;
	    """, (data,))
	    vendas = self.cursor.fetchall()

	    print(f'{"-"*160}\n{"VENDAS DO DIA":^160}\n{"-"*160}')
	    print(f'{"ID":4} | {"NOME":20} | {"QUANTIDADE":10} | {"VALOR":5} | {"TOTAL":5} | {"DATA":10} | {"HORA"}')
	    print(f'{"-"*160}')
	    for venda in vendas:
	        print(f'{venda[0]:4} | {venda[1]:20} | {venda[2]:10} | {venda[3]:5} | {venda[4]:5} | {venda[5]:10} | {venda[6]}')
	        total += venda[4]
	    print(f'O total vendido R${total:.2f}')


	def ver_vendas(self) -> None:
	    """
	    Recupera todos os registros da tabela 'vendas' e os imprime.
	    :param self:
	    :return:
	    """
	    total = 0
	    self.cursor.execute("""
	    SELECT * FROM vendas;
	    """)
	    vendas = self.cursor.fetchall()

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
4 - DEMITIR FUNCIONÁRIOS
5 - SAIR\n{"-"*160}
    """)


def sistema_adm():
	conn = sqlite3.connect('database/gerentia.db')
	cursor = conn.cursor()
	BD = BD_Funcionarios(cursor)

	continuar = True
	while continuar:
		menu()
		opcao = int(input('Escolha a opção desejada: '))

		if opcao == 1:
			BD.cadastrar_funcionario()
		elif opcao == 2:
            		BD.alterar_dados()
		elif opcao == 3:
			BD.mostrar_funcionarios()
		elif opcao == 4:
			BD.demitir_funcionario()
		elif opcao == 5:
			BD.log('usuario', 'saiu do sistema')
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
