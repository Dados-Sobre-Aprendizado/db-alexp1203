import os
import pandas as pd
import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(os.environ["postgresql://sys-user:reezzjdJr-2ORsgr2CK4hQ@artful-elf-13228.j77.aws-us-east-1.cockroachlabs.cloud:26257/livrariadb?sslmode=verify-full"])

@contextmanager
def get_cursor(commit=False):
    """
    Exemplo:
        with get_cursor() as cur:
            cur.execute("SELECT * FROM livros")
            
    """
    conn = get_conn()
    cur = conn.cursor()
    try:
        yield cur
        if commit:
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


"""
conecxão com banco web

"Driver={SQL Server Native Client 11.0};"
                      "Server=server_name;"
                      "Database=db_name;"
                      "Trusted_Connection=yes;"
                      
                      """