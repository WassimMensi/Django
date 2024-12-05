import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mabase",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
