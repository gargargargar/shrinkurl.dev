import string
import random
from secrets import token_urlsafe

default_length = 6

def _generate_shrinked_url():
    return token_urlsafe(int(default_length / 1.3))

# def shrink_url(url: str):
#     if url in self.url_to_short:
#         # Return already-generated short url
#         return self.url_to_short[url]

#     # Generate new short url
#     short_url = self._generate_short_url()
#     while short_url in self.short_to_url:
#         short_url = self._generate_short_url()

#     # TODO: replace with db commands
#     self.url_to_short[url] = short_url
#     self.short_to_url[short_url] = url

#     return short_url

# def redirect_url(shrinked_url: str):
#     if short_url in self.short_to_url:
#         return self.short_to_url[short_url]

#     return '404 Error'

if __name__ == '__main__':
    for i in range(10):
        print(_generate_shrinked_url())
    # short_url_1 = url_shortener.create_url('google.com')
    # short_url_2 = url_shortener.create_url('facebook.com')
    # short_url_3 = url_shortener.create_url('piccollage.com')
    # short_url_4 = url_shortener.create_url('yahoo.com')

    # print(short_url_1, short_url_2, short_url_3, short_url_4)

    # print(url_shortener.return_url(short_url_1))
    # print(url_shortener.return_url(short_url_2))
    # print(url_shortener.return_url(short_url_3))
    # print(url_shortener.return_url(short_url_4))

    # short_url_5 = url_shortener.create_url('facebook.com')
    # print(short_url_5)
    # print(url_shortener.return_url(short_url_5))

    # print(url_shortener.return_url('errort'))
