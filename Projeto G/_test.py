import sqlite3
import requests

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
        

def request_to_api():
    try:
        request = {
        	"cod": "1234583",
        	"nome": "produto aleatorio 333",
        	"descricao": "qual quer coisa 333",
        	"quantidade": 15,
        	"preco_compra": 7.95,
        	"preco_venda": 15.40,
        	"data_atual": "2023-11-15",
        	"hora_atual": "12:30:00",
        	"status": 5,
        	"sincronizado": 1
        }
        
        res = requests.post(f'http://localhost:8000/api/stock/sinc', json=request)
    except requests.exceptions.ConnectionError as err:
        return err
    else:
        if res.status_code == 200:
            # Requisição feita com sucesso
            return 1
        # Requisição com erros
        return res.json()

def __test__():
    result = request_to_api()
    if type(result) is not requests.exceptions.ConnectionError:
        for key, value in result.items():
            print(f'{key} = {value}')
    else:
        print(result.args[0])
    
    

if __name__ == "__main__":
    __test__()
