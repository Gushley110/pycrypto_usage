import base64

def url_to_base64(url):
    return base64.urlsafe_b64encode(url.encode())

def base64_to_str(base64_string):
    return base64.urlsafe_b64decode(base64_string).decode()

test_string = 'https://open.spotify.com/collection/tracks'
encoded = url_to_base64(test_string)

print(encoded)

print(base64_to_str(encoded))