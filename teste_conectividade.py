import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

conn = psycopg2.connect(os.environ["postgresql://sys-user:reezzjdJr-2ORsgr2CK4hQ@artful-elf-13228.j77.aws-us-east-1.cockroachlabs.cloud:26257/livrariadb?sslmode=verify-full"])
with conn.cursor() as cur:
    cur.execute("SELECT * FROM public.livros LIMIT 5;")
    print(cur.fetchone())