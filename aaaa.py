import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def criar_conexao():
    conn = psycopg2.connect(
        host=os.envirom.get("DB_HOST"),
        database=os.envirom.get("DB_NAME"),
        user=os.envirom.get("DB_USER"),
        password=os.envirom.get("DB_PASSWORD"),
    )
    return conn