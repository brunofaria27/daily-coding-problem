'''
shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
'''
import random
import string

url_map = {}

def shorten(url):
    short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url_map[short_id] = url
    return short_id

def restore(short):
    url = url_map.get(short)
    
    if url is not None:
        return url
    else:
        return None
    
url1 = 'https://www.example.com'
short1 = shorten(url1)
assert len(short1) == 6
assert restore(short1) == url1
    
url2 = 'https://www.google.com'
short2 = shorten(url2)
assert len(short2) == 6
assert restore(short2) == url2