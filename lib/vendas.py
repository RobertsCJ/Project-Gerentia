import sqlite3
from datetime import datetime
from lib.estoque import ver_estoque


def criar_tabela_vendas(cursor) -> None:
    """
    Cria uma tabela chamada 'vendas' no banco de dados SQLite se ela ainda não existir.
    A tabela inclui colunas para ID da venda, nome do produto, quantidade vendida, valor unitário do produto,
    valor total da venda, data e hora da venda.
    :param cursor:
    :return:
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL,
        total REAL NOT NULL,
        data DATE DEFAULT CURRENT_DATE,
        hora TIME DEFAULT CURRENT_TIME
    );
    """)


def ver_vendas_do_dia(cursor) -> None:
    """
    Recupera todos os registros da tabela 'vendas' que têm a data atual e os imprime.
    :param cursor:
    :return:
    """
    cursor.execute("""
    SELECT * FROM vendas WHERE data = CURRENT_DATE;
    """)
    vendas = cursor.fetchall()

    total = 0
    print(f'{"-"*160}\n{"VENDAS DO DIA":^160}\n{"-"*160}')
    print(f'{"ID":4} | {"NOME":20} | {"QUANTIDADE":10} | {"VALOR":5} | {"TOTAL":5} | {"DATA":10} | {"HORA"}')
    print(f'{"-"*160}')
    for venda in vendas:
        print(f'{venda[0]:4} | {venda[1]:20} | {venda[2]:10} | {venda[3]:5} | {venda[4]:5} | {venda[5]:10} | {venda[6]}')
        total += venda[4]
    print(f'O lucro do dia R${total:.2f}.')


def estorno(cursor) -> None:
    """
    Solicita ao usuário que insira um ID de venda e um código de produto. Em seguida, recupera a quantidade vendida
    e a quantidade atual do produto no estoque. Se a venda e o produto existirem, atualiza a quantidade do produto
    no estoque e exclui a venda.
    :param cursor:
    :return:
    """
    ver_estoque(cursor)
    ver_vendas_do_dia(cursor)
    id_venda = input('Digite o ID da venda: ')
    cod_estoque = input('Digite o código do produto no estoque: ')

    cursor.execute("""
    SELECT nome, quantidade FROM vendas WHERE id = ?;
    """, (id_venda,))
    dados_venda = cursor.fetchone()

    if dados_venda is None:
        print("Venda não encontrada.")
        return

    nome_venda, quantidade_venda = dados_venda

    cursor.execute("""
    SELECT quantidade FROM estoque WHERE cod = ?;
    """, (cod_estoque,))
    dados_estoque = cursor.fetchone()

    if dados_estoque is None:
        print("Produto não encontrado no estoque.")
        return

    quantidade_estoque = dados_estoque[0]

    nova_quantidade = quantidade_estoque + quantidade_venda
    cursor.execute("""
    UPDATE estoque SET quantidade = ? WHERE cod = ?;
    """, (nova_quantidade, cod_estoque))

    cursor.execute("""
    DELETE FROM vendas WHERE id = ?;
    """, (id_venda,))

    print(f'Estorno realizado com sucesso! A quantidade de {nome_venda} no estoque agora é {nova_quantidade}.')
    log(nome_usuario, 'X produto estornado')

def realizar_venda(cursor) -> None:
    """
    Solicita ao usuário que insira o nome e a quantidade de um produto. Em seguida, verifica se o produto existe na tabela 'estoque'
    e se há quantidade suficiente em estoque. Se o produto existir e houver quantidade suficiente, calcula o valor total da venda
    e insere um registro na tabela 'vendas'. Em seguida, atualiza a quantidade do produto na tabela 'estoque'.
    Se a quantidade se tornar zero, exclui o registro correspondente da tabela 'estoque'.
    :param cursor:
    :return:
    """
    criar_tabela_vendas(cursor)
    nome = str(input('Nome do produto: ')).strip().upper()
    quantidade = int(input('Quantidade: '))

    cursor.execute("""
    SELECT quantidade, preco_venda FROM estoque WHERE nome = ?;
    """, (nome,))
    dados = cursor.fetchone()

    if dados is None:
        print("Produto não encontrado.")
        return

    quantidade_estoque, preco_venda = dados
    if quantidade > quantidade_estoque:
        print(f"Quantidade insuficiente no estoque. Disponível: {quantidade_estoque}")
        return

    total = quantidade * preco_venda
    hora_atual = datetime.now().strftime('%H:%M:%S')
    cursor.execute("""
    INSERT INTO vendas (nome, quantidade, valor, total, data, hora)
    VALUES (?, ?, ?, ?, CURRENT_DATE, ?)
    """, (nome, quantidade, preco_venda, total, hora_atual))

    nova_quantidade = quantidade_estoque - quantidade
    if nova_quantidade == 0:
        cursor.execute("""
        DELETE FROM estoque WHERE nome = ?;
        """, (nome,))
    else:
        cursor.execute("""
        UPDATE estoque SET quantidade = ? WHERE nome = ?;
        """, (nova_quantidade, nome))

    print(f'Venda realizada com sucesso! Total: {total}')
    log(nome_usuario, 'X produto vendido')

def encontrar_produto(cursor):
    """
    Encontra um produto no estoque por nome ou descrição.
    Solicita ao usuário que escolha entre pesquisar por nome ou descrição e, em seguida, insira o termo de pesquisa.
    Recupera todos os registros da tabela 'estoque' que têm o nome ou a descrição especificados e os imprime.
    :param cursor: Cursor do SQLite para executar consultas SQL
    """
    escolha = input('Você deseja pesquisar por nome ou descrição? ')
    termo_de_pesquisa = input('Digite o termo de pesquisa: ').strip().upper()

    if escolha.lower() == 'nome':
        cursor.execute("""
        SELECT * FROM estoque WHERE nome = ?;
        """, (termo_de_pesquisa,))
    elif escolha.lower() == 'descrição':
        cursor.execute("""
        SELECT * FROM estoque WHERE descricao = ?;
        """, (termo_de_pesquisa,))

    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)


def menu():
    print(f"""
{"-" * 160}\n{"MENU":^160}\n{"-" * 160}
1 - VENDER
2 - ENCONTRAR PRODUTO
3 - ESTORNO
4 - VER LUCRO DO DIA
5 - SAIR
{"-" * 160}
""")


def sistema_vendas():
    conn = sqlite3.connect('data/gerentia.db')
    cursor = conn.cursor()

    continuar = True
    while continuar:
        menu()
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            realizar_venda(cursor)
        elif opcao == 2:
            encontrar_produto(cursor)
        elif opcao == 3:
            estorno(cursor)
        elif opcao == 4:
            ver_vendas_do_dia(cursor)
        elif opcao == 5:
            continuar = False
        else:
            print('ERRO! Opção inválida.')

        conn.commit()
    conn.close()

