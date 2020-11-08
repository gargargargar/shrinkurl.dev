import os
import psycopg2


def create_table():
    # DATABASE_URL = os.environ['DATABASE_URL']
    DATABASE_URL = "postgres://gtellzbmkxrytl:418b6e0bd48ce2944213cb9b9612326dcc49983d1174188e789ca92e9c37bb92@ec2-23-23-36-227.compute-1.amazonaws.com:5432/ddj1qckct2jsm2"
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    create_command = """
        CREATE TABLE urls (
            url VARCHAR(2083) NOT NULL,
            shrinked_hash VARCHAR(20) NOT NULL,
            PRIMARY KEY (url)
        )
        """

    cur = conn.cursor()
    cur.execute(create_command)

    cur.close()
    conn.close()

if __name__ == '__main__':
    create_table()    
