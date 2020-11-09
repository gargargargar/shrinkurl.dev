import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

def execute_non_query(command: str):
    cursor.execute(command)
    conn.commit()

def execute_query(command: str):
    cursor.execute(command)
    return cursor.fetchall()

def create_table():
    create_command = """
        CREATE TABLE urls (
            url VARCHAR(2083) NOT NULL,
            shrinked_hash VARCHAR(20) NOT NULL UNIQUE,
            PRIMARY KEY (url)
        )
        """
    execute_non_query(create_command)

def get_shrinked_hash(url: str):
    query = f"""
        SELECT shrinked_hash FROM urls WHERE url = '{url}'
    """

    result = execute_query(query)
    if len(result) == 0:
        return None
    return result[0][0]

def get_url(shrinked_hash: str):
    query = f"""
        SELECT url FROM urls WHERE shrinked_hash = '{shrinked_hash}'
    """

    result = execute_query(query)
    if len(result) == 0:
        return None
    return result[0][0]

def insert_url(url: str, shrinked_hash: str):
    if get_shrinked_hash(url) is not None or get_url(shrinked_hash) is not None:
        print('Insertion failed.')
        return False

    non_query = f"""
        INSERT INTO urls
        VALUES ('{url}', '{shrinked_hash}')
    """
    execute_non_query(non_query)

    return True

if __name__ == '__main__':
    create_table()
    # insert_url('test1', 'abcdef')
    # insert_url('test2', 'abdejjk')
    # insert_url('test2', 'adnjdd')

    # print(get_shrinked_hash('test1'))
    # print(get_shrinked_hash('test2'))
    # print(get_url('abcdef'))

    cursor.close()
    conn.close()