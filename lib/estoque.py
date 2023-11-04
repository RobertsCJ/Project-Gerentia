import sqlite3
import uuid
from datetime import datetime
from lib.adm import *


def criar_tabela(cursor) -> None:
        """
	Cria uma tabela chamada 'estoque' no banco de dados se ela ainda não existir.
	A tabela inclui colunas para código do produto, nome, descrição, quantidade, preço de compra,
	preço de venda, data atual e hora atual.
	:param cursor: Cursor do SQLite para executar consultas SQL
	:return:
	"""
	cursor.execute("""
	CREATE TABLE IF NOT EXISTS estoque (
	cod NOT NULL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	descricao TEXT,
	quantidade INTEGER,
	preco_compra REAL,
	preco_venda REAL,
	data_atual DATE DEFAULT CURRENT_DATE,
	hora_atual TIME DEFAULT CURRENT_TIME
	);
	""")

class Produto:
	def __init__(self, cod, nome, descricao, quantidade, preco_compra, preco_venda, hora_atual):
		self.cod = cod
		self.nome = nome
		self.descricao = descricao
		self.quantidade = quantidade
		self.preco_compra = preco_compra
		self.preco_venda = preco_venda
		self.hora_atual = hora_atual

class BD_Estoque:
	def __init__(self, cursor):
		self.cursor = cursor

	def adicionar_prod(self) -> None:
		"""
		Adiciona um produto ao estoque. Solicita ao usuário que insira detalhes sobre o produto
		(nome, descrição, quantidade, preço de compra, preço de venda), gera um código único para o produto
		usando o módulo uuid e insere esses detalhes na tabela 'estoque'.
		:param self:
		:return:
		"""
		criar_tabela(self.cursor)
		cod = str(uuid.uuid4())
		nome = str(input('Nome do produto: ')).strip().upper()
		descricao = str(input('Descrição: ')).strip().upper()
		quantidade = int(input('Quantidade: '))
		preco_compra = float(input('Preço de compra: '))
		preco_venda = float(input('Preço de venda: '))
		hora_atual = datetime.now().strftime('%H:%M:%S')
		produto = Produto(cod, nome, descricao, quantidade, preco_compra, preco_venda, hora_atual)

		self.cursor.execute("""
		INSERT INTO estoque (cod, nome, descricao, quantidade, preco_compra, preco_venda, data_atual, hora_atual)
		VALUES (?, ?, ?, ?, ?, ?, CURRENT_DATE, ?)
		""", (produto.cod, produto.nome, produto.descricao, produto.quantidade, produto.preco_compra, produto.preco_venda, produto.hora_atual))
		log('user', 'produto X adicionado')

	def ver_estoque(self) -> None:
	    """
	    Recupera todos os registros da tabela 'estoque' e os imprime.
	    :param cursor:
	    :return:
	    """
	    self.cursor.execute("""
	    SELECT * FROM estoque;
	    """)
	    dados = self.cursor.fetchall()

	    print(f'{"-"*160}\n{"PRODUTOS EM ESTOQUE":^160}\n{"-"*160}')
	    print(f'{"CÓD":36} | {"NOME":20} | {"DESCRIÇÃO":20} | {"QUANTIDADE":10} | {"PREÇO DE COMPRA":15} | ', end='')
	    print(f'{"PREÇO DE VENDA":14} | {"DATA":10} | {"HORA"}')
	    print('-'*160)
	    for dado in dados:
	        print(f'{dado[0]:36} | {dado[1]:20} | {dado[2]:20} | {dado[3]:10} | {dado[4]:<15} | {dado[5]:<14} | {dado[6]} | {dado[7]}')


	def excluir_produto(self) -> None:
	    """
	    Solicita ao usuário que insira um código de produto e exclui o registro correspondente do banco de dados.
	    :param cursor:
	    :return:
	    """
	    ver_estoque(self.cursor)
	    print(f'{"-" * 160}\n{"EXCLUIR PRODUTO":^160}\n{"-" * 160}')
	    cod = str(input('Qual o código de barras do produto: ')).strip()
	    self.cursor.execute("""
	    DELETE FROM estoque WHERE cod = ?;
	    """, (cod,))
	    print(f'{"-" * 160}\n{"PRODUTO EXCLUÍDO":^160}\n{"-" * 160}')
	    log('user', 'produto X excluido')

	def atualizar_produto(self) -> None:
	    """
	    Solicita ao usuário que insira detalhes sobre um produto (nome, descrição, quantidade, preço de compra, preço de venda) e um código de produto.
	    Em seguida, atualiza o registro correspondente na tabela 'estoque'.
	    :param cursor:
	    :return:
	    """
	    print(f'{"-" * 160}\n{"ATUALIZAR PRODUTO":^160}\n{"-" * 160}')
	    cod = str(input('Qual o código de barras do produto? ')).strip()
	    nome = str(input('Nome do produto: ')).strip().upper()
	    descricao = str(input('Descrição: ')).strip().upper()
	    quantidade = int(input('Qantidade: '))
	    preco_compra = float(input('Preço de compra: '))
	    preco_venda = float(input('Preço de venda: '))
            produto = Produto(cod, nome, descricao, quantidade, preco_compra, preco_venda)	    

            self.cursor.execute("""
	    UPDATE estoque SET nome = ?, descricao = ?, quantidade = ?, preco_compra = ?, preco_venda = ? WHERE cod = ?;
	    """, (produto.nome, produto.descricao, produto.quantidade, produto.preco_compra, produto.preco_venda, produto.cod))
	    print(f'{"-" * 160}\n{"ATUALIZADO COM SUCESSO!":^160}\n{"-" * 160}')
	    log('user', f'{produto.nome} atualizado')

def menu():
    print(f"""
{"-"*160}\n{"MENU ESTOQUE":^160}\n{"-"*160}
1 - ADICIONAR UM PRODUTO
2 - VER ESTOQUE
3 - EXCLUIR PRODUTO
4 - ATUALIZAR PRODUTO
5 - SAIR
{"-"*160}
""")


def sistema_estoque():
    conn = sqlite3.connect('database/gerentia.db')
    cursor = conn.cursor()
    BD = BD_Estoque(cursor)

    continuar = True
    while continuar:
        menu()
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            BD.adicionar_prod()
        elif opcao == 2:
            BD.ver_estoque()
        elif opcao == 3:
            BD.excluir_produto()
        elif opcao == 4:
            BD.atualizar_produto()
        elif opcao == 5:
            log('usuario', 'saiu do sistema')
            continuar = False
        else:
            print('ERRO: Opção inválida!')
        conn.commit()
    conn.close()
