###################################################
#
# POR: WALLYSON S. SOUZA, ROBERTO CARLOS e JONATAS N. FREITAS
# PROJETO DESENVOLVIDO COM: Qt Designer e PySide6
# V: 1.0.0
#
###################################################
import sqlite3

class DB_Gerentia:
    def __init__(self, nome="gerentia.db") -> None:
        self.nome = nome

    def conexao(self):
        self.conn = sqlite3.connect(self.nome)

    def fechar_conexao(self):
        try:
            self.conn.close()
        except EOFError as Er:
            pass

    def criar_tabela(self):

        cursor = self.conn.cursor()
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

    def cadastrar_produto(self, dadosProduto):

        campos_tabela = ('cod', 'nome', 'descricao', 'quantidade', 'preco_compra', 'preco_venda', 'data_atual', 'hora_atual')

        qntd = ('?,?,?,?,?,?,?,?')
        cursor = self.conn.cursor()

        try:
            cursor.execute(f"""
            INSERT INTO estoque {campos_tabela} 
            VALUES({qntd})""", dadosProduto)
            self.conn.commit()
            return "OK"
        except:
            return "Erro"

    def mostrar_produtos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM estoque")
            estoque = cursor.fetchall()
            return estoque
        except Exception as e:
            print(f"Ocorreu um erro ao recuperar produtos: {e}")
            return None

    def excluir_estoque(self, cod):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"DELETE FROM estoque WHERE cod = '{cod}'")
            self.conn.commit()
            return "Cadastro excluído com sucesso!"
        except:
            return "Erro ao excluir registro!"

    def alterar_produto(self, dadosProduto):

        cursor = self.conn.cursor()

        cursor.execute(f""" UPDATE estoque set
            cod = '{dadosProduto[0]}',
            nome = '{dadosProduto[1]}',
            descricao = '{dadosProduto[2]}',
            quantidade = '{dadosProduto[3]}',
            preco_compra = '{dadosProduto[4]}',
            preco_venda = '{dadosProduto[5]}',
            data_atual = '{dadosProduto[6]}',
            hora_atual = '{dadosProduto[7]}'
            
            WHERE cod = '{dadosProduto[0]}'""")

        self.conn.commit()

    def mostrar_produto_especifico(self, pesquisa):
        try:
            cursor = self.conn.cursor()
            # Usando o operador LIKE para pesquisa insensível a maiúsculas e minúsculas
            cursor.execute("SELECT * FROM estoque WHERE nome LIKE ? OR descricao LIKE ?", ('%' + pesquisa + '%', '%' + pesquisa + '%'))
            produtos = cursor.fetchall()
            return produtos
        except Exception as e:
            print(f"Ocorreu um erro ao recuperar produtos: {e}")
            return None
    