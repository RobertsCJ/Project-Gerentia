import sqlite3

def list_all():
    conn = sqlite3.connect("gerentia.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tb_estoque WHERE status != 2")
    result = cursor.fetchall()
    estoques = list()
    for data in result:
        estoque = dict()
        estoque['cod'] = data[0]
        estoque['nome'] = data[1]
        estoque['descricao'] = data[2]
        estoque['quantidade'] = data[3]
        estoque['preco_compra'] = data[4]
        estoque['preco_venda'] = data[5]
        estoque['data_atual'] = data[6]
        estoque['hora_atual'] = data[7]
        estoque['status'] = data[8]
        estoque['sincronizado'] = data[9]
        estoques.append(estoque)
    
    return estoques

def mostrar_produtos(estoques):
    for estoque in estoques:
        for key, value in estoque.items():
            print(f'{key} = {value}')
        
def __test__():
    estoques = list_all()
    mostrar_produtos(estoques)
    

if __name__ == "__main__":
    __test__()

