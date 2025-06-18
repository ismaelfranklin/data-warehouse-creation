import pandas as pd
from connection import conectar

def carregar_fato_vendas(conn):
    df = pd.read_csv('data/vendas.csv')
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO fato_vendas (
                id_cliente, id_produto, data_venda,
                quantidade, preco_unitario, valor_total
            )
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (
            row['id_cliente'],
            row['id_produto'],
            row['data_venda'],
            row['quantidade'],
            row['preco_unitario'],
            row['valor_total']
        ))

    conn.commit()
    print("fato_vendas carregada com sucesso.")

if __name__ == "__main__":
    conn = conectar()
    if conn:
        carregar_fato_vendas(conn)
        conn.close()
        print("Conexão fechada.")
    else:
        print("Falha ao estabelecer conexão.")