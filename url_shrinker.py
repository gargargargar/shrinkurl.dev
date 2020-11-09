import string
import validators
import secrets
import db

default_length = 6

def _generate_shrinked_hash():
    alphabet = string.ascii_letters + string.digits

    result = ''.join(secrets.choice(alphabet) for _ in range(default_length))
    if db.get_url(result) is not None:
        result = ''.join(secrets.choice(alphabet) for _ in range(default_length))

    return result

def _validate_url(url: str):
    # TODO: find better way; this ignores urls without https://
    return validators.url(url)

def _validate_hash(shrinked_hash: str): 
    return shrinked_hash is not None and len(shrinked_hash) <= default_length and shrinked_hash.isalnum()

def shrink_url(url: str):
    # Check if url is legal
    if not _validate_url(url):
        print('Url is not valid!')
        return None

    # Check if url exists in db and return hash if it does
    query_result = db.get_shrinked_hash(url)
    if query_result is not None:
        return query_result

    # Generate new short url
    shrinked_hash = _generate_shrinked_hash()

    # Insert into db
    db.insert_url(url, shrinked_hash)

    return shrinked_hash

def redirect_shrinked_hash(shrinked_hash: str):
    # Check if shrinked_hash is legal
    if not _validate_hash(shrinked_hash):
        return None

    return db.get_url(shrinked_hash)

if __name__ == '__main__':
    for i in range(10):
        print(_generate_shrinked_hash())
    short_url_1 = shrink_url('https://google.com')
    short_url_2 = shrink_url('https://facebook.com')
    short_url_3 = shrink_url('https://piccollage.com')
    short_url_4 = shrink_url('https://yahoo.com')

    print(short_url_1, short_url_2, short_url_3, short_url_4)

    print(redirect_shrinked_hash(short_url_1))
    print(redirect_shrinked_hash(short_url_2))
    print(redirect_shrinked_hash(short_url_3))
    print(redirect_shrinked_hash(short_url_4))

    short_url_5 = shrink_url('https://facebook.com')
    print(short_url_5)
    print(redirect_shrinked_hash(short_url_5))

    print(redirect_shrinked_hash('errort'))
