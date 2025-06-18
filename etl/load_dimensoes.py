import pandas as pd
from connection import conectar

def carregar_dim_cliente(conn):
    df = pd.read_csv('data/clientes.csv')
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO dim_cliente (id_cliente, nome, cidade)
            VALUES (%s, %s, %s)
            ON CONFLICT (id_cliente) DO NOTHING;
        """, (row['id_cliente'], row['nome'], row['cidade']))

    conn.commit()
    print("dim_cliente carregada com sucesso.")


def carregar_dim_produto(conn):
    df = pd.read_csv('data/produtos.csv')
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO dim_produto (id_produto, nome_produto, categoria)
            VALUES (%s, %s, %s)
            ON CONFLICT (id_produto) DO NOTHING;
        """, (row['id_produto'], row['nome_produto'], row['categoria']))

    conn.commit()
    print("dim_produto carregada com sucesso.")


def carregar_dim_tempo(conn):
    df = pd.read_csv('data/datas.csv')
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO dim_tempo (data_id, data_venda)
            VALUES (%s, %s)
            ON CONFLICT (data_id) DO NOTHING;
        """, (row['data_id'], row['data_venda']))

    conn.commit()
    print("dim_tempo carregada com sucesso.")
