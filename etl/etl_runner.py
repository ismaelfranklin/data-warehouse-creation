from connection import conectar
from load_dimensoes import carregar_dim_cliente, carregar_dim_produto, carregar_dim_tempo
from load_fato import carregar_fato_vendas

conn = conectar()

if conn:
    carregar_dim_cliente(conn)
    carregar_dim_produto(conn)
    carregar_dim_tempo(conn)
    carregar_fato_vendas(conn)
    conn.close()
