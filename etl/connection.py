import psycopg2
from dotenv import load_dotenv
import os
import logging
from typing import Optional
from psycopg2.extensions import connection

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'dbname': os.getenv('DB_NAME', 'dw_vendas'),
    'user': os.getenv('DB_USER', 'frank'),
    'password': os.getenv('DB_PASSWORD', ''),
    'port': os.getenv('DB_PORT', '5432')
}

def get_connection() -> Optional[connection]:
    """Establish PostgreSQL database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logger.info("Database connection successful")
        return conn
    except psycopg2.Error as e:
        logger.error(f"Database connection error: {e}")
        return None

def fechar_conexao(conn: Optional[connection]) -> None:
    """
    Fecha a conexão com o banco de dados de forma segura.
    
    Args:
        conn (Optional[connection]): Conexão a ser fechada
    """
    if conn:
        try:
            conn.close()
            logger.info("Conexão fechada com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao fechar conexão: {e}")

if __name__ == "__main__":
    conn = get_connection()
    fechar_conexao(conn)