from lib.adm import *
from lib.estoque import *
from lib.vendas import *
from lib import intro
import sqlite3


def login(cursor) -> None:
    """
    Realiza o login de um usuário no sistema.
    :return: None
    """
    nome_usuario = str(input('Informe o nome de usuário: '))
    senha = pwinput.pwinput('Informe a senha: ')
    cursor.execute("""
    SELECT * FROM funcionarios WHERE nome_usuario = ? AND senha = ?;
    """, (nome_usuario, senha))
    usuario = cursor.fetchone()

    if usuario is not None:
        if usuario[2] == 'Administrador':
            sistema_adm()
        if usuario[2] == 'Estoque':
            sistema_estoque()
        elif usuario[2] == 'Vendedor':
            sistema_vendas()
    else:
        print('Usuário ou senha inválidos.')


def iniciar_sistema():
    conn = sqlite3.connect('database/gerentia.db')
    cursor = conn.cursor()
    login(cursor)
    conn.commit()
    conn.close()


if __name__ == "__main__":    
	iniciar_sistema()
