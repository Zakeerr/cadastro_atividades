import psycopg2


def conectar():

    conexao = psycopg2.connect(
        host="localhost",
        database="organizaja",
        user="postgres",
        password="2004"
    )

    return conexao