#!/bin/bash

# Caminho para o arquivo do banco de dados SQLite
DATABASE_PATH="../gerentia.db"

# Array contendo as queries para criar tabelas
TABLE_QUERIES=(
    "CREATE TABLE IF NOT EXISTS tb_funcionarios (
        matricula varchar(32) PRIMARY KEY,
        nome varchar(255) NOT NULL,
        cargo varchar(255) NOT NULL,
        nome_usuario varchar(255) NOT NULL,
        senha varchar(255) NOT NULL,
        data_atual DATE DEFAULT CURRENT_DATE, 
        hora_atual TIME DEFAULT CURRENT_TIME,
        status numeric NOT NULL,
        sincronizado numeric NOT NULL
    );"
    "CREATE TABLE IF NOT EXISTS tb_estoque (
        cod varchar(32) PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        descricao TEXT NOT NULL, 
        quantidade INTEGER NOT NULL, 
        preco_compra REAL NOT NULL, 
        preco_venda REAL NOT NULL, 
        data_atual DATE DEFAULT CURRENT_DATE, 
        hora_atual TIME DEFAULT CURRENT_TIME,
        status numeric NOT NULL,
        sincronizado numeric NOT NULL
    );"
)

# Itera sobre as queries e executa cada uma
for QUERY in "${TABLE_QUERIES[@]}"
do
    sqlite3 $DATABASE_PATH "$QUERY"
done

echo "Operação concluída: Todas as tabelas foram recriadas no banco de dados."
