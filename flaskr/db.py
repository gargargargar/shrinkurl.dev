import os
import psycopg2



def create_table():
    DATABASE_URL = os.environ['DATABASE_URL']
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
