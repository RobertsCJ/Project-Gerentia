######################################################################
#
# POR: WALLYSON S. SOUZA, ROBERTO CARLOS e JONATAS N. FREITAS
# PROJETO DESENVOLVIDO COM: Qt Designer e PySide6
# V: 1.0.0
#
#####################################################################
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
            	CREATE TABLE IF NOT EXISTS tb_estoque (
            	cod NOT NULL PRIMARY KEY,
            	nome VARCHAR(100) NOT NULL,
            	descricao TEXT,
            	quantidade INTEGER,
            	preco_compra REAL,
            	preco_venda REAL,
            	data_atual DATE DEFAULT CURRENT_DATE,
            	hora_atual TIME DEFAULT CURRENT_TIME,
                status NUMERIC,
                sincronizado NUMERIC
            	);
            	""")

    def cadastrar_produto(self, dadosProduto):

        campos_tabela = ('cod', 'nome', 'descricao', 'quantidade',
                         'preco_compra', 'preco_venda', 'data_atual', 'hora_atual', 'status', 'sincronizado')

        qntd = ('?,?,?,?,?,?,?,?,?,?')
        cursor = self.conn.cursor()

        try:
            cursor.execute(f"""
            INSERT INTO tb_estoque {campos_tabela} 
            VALUES({qntd})""", dadosProduto)
            self.conn.commit()
            return "OK"
        except Exception as error:
            return error

    def mostrar_produtos(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM tb_estoque")
            estoque = cursor.fetchall()
            return estoque
        except Exception as e:
            print(f"Ocorreu um erro ao recuperar produtos: {e}")
            return None

    def excluir_estoque(self, cod):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"DELETE FROM tb_estoque WHERE cod = '{cod}'")
            self.conn.commit()
            return "Cadastro excluído com sucesso!"
        except:
            return "Erro ao excluir registro!"

    def alterar_produto(self, dadosProduto):

        cursor = self.conn.cursor()

        cursor.execute(f""" UPDATE tb_estoque set
            cod = '{dadosProduto[0]}',
            nome = '{dadosProduto[1]}',
            descricao = '{dadosProduto[2]}',
            quantidade = '{dadosProduto[3]}',
            preco_compra = '{dadosProduto[4]}',
            preco_venda = '{dadosProduto[5]}',
            data_atual = '{dadosProduto[6]}',
            hora_atual = '{dadosProduto[7]}',
            status = 1,
            sincronizado = 0
            
            WHERE cod = '{dadosProduto[0]}'""")

        self.conn.commit()

    def atualizar_sincronizado(self, cod):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE tb_estoque SET sincronizado = 1 WHERE cod = ? and sincronizado = 0", (cod,))
        self.conn.commit()

    def mostrar_produto_especifico(self, pesquisa):
        try:
            cursor = self.conn.cursor()
            # Usando o operador LIKE para pesquisa insensível a maiúsculas e minúsculas
            cursor.execute("SELECT * FROM tb_estoque WHERE nome LIKE ? OR descricao LIKE ?",
                           ('%' + pesquisa + '%', '%' + pesquisa + '%'))
            produtos = cursor.fetchall()
            return produtos
        except Exception as e:
            print(f"Ocorreu um erro ao recuperar produtos: {e}")
            return None

    def criar_tabela_funcionarios(self):

        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tb_funcionarios (
            matricula NOT NULL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cargo VARCHAR(100),
            nome_usuario VARCHAR(100),
            senha VARCHAR(25),
            status NUMERIC,
            sincronizado NUMERIC
        );
        """)

    def cadastrar_usuario(self, dadosUsuario):

        campos_tabela = ('matricula', 'nome', 'cargo',
                         'nome_usuario', 'senha', 'status', 'sincronizado')

        qntd = ('?,?,?,?,?,?,?')
        cursor = self.conn.cursor()

        try:
            cursor.execute(f"""
            INSERT INTO funcionarios {campos_tabela} 
            VALUES({qntd})""", dadosUsuario)
            self.conn.commit()
            return "OK"
        except:
            return "Erro"

    def remover_funcionario(self, matricula, nome):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"SELECT nome FROM tb_funcionarios WHERE matricula = '{matricula}'")
            result = cursor.fetchone()
            if result is None:
                return "Matrícula não encontrada!"
            elif result[0] != nome:
                return f"O nome não corresponde à matrícula! O nome da matrícula é {result[0]} e não {nome}."
            else:
                cursor.execute(
                    f"DELETE FROM tb_funcionarios WHERE matricula = '{matricula}'")
                self.conn.commit()
                return "Usuário excluído com sucesso!"
        except Exception as e:
            print(e)
            return "Erro ao excluir registro!"

    def adicionar_admin_padrao(self):
        try:
            cursor = self.conn.cursor()
            # Verifica se o administrador padrão já existe
            cursor.execute(
                "SELECT matricula FROM tb_funcionarios WHERE matricula = 'admin'")
            result = cursor.fetchone()
            # Se o administrador padrão não existir, o sistema adiciona
            if result is None:
                cursor.execute("""
                    INSERT INTO tb_funcionarios (matricula, nome, cargo, nome_usuario, senha, status, sincronizado) 
                    VALUES ('admin', 'Admin', 'Administrador', 'admin', 'admin123', 0, 0)
                """)
                self.conn.commit()
                print("Administrador padrão adicionado com sucesso!")
            else:
                print("O administrador padrão já existe.")
        except Exception as e:
            print(e)

    def verificar_login(self, usuario, senha):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """SELECT * FROM tb_funcionarios WHERE nome_usuario = ? AND senha = ?""", (usuario, senha))

            usuarios = cursor.fetchall()
            if len(usuarios) > 0:
                return "Usuário validado!"
            else:
                return "Usuário não inválido!"
        except Exception as e:
            return f"Erro! {e}"
