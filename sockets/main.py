import socket

URLS = {'/': 'Hello index',
        '/blog': 'hello blog'}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    if not method == 'GET':
        return ('http / 405 method not allowed\n\n', 405)

    if not url in URLS:
        return ('http / 404 not found \n\n', 404)

    return ('HTTP 200', 200)

def generate_content(code,url):
    if code == 404:
        return '<h1> code 404 </h1><p>not fouud</p>'
    if code == 405:
        return '<h1> code 405 </h1><p>not allowed</p>'
    return '<h1>{}</h1>'.format(URLS[url])


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code,url)

    return (headers + body).encode()


def run():
    server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socker.bind(('localhost', 5000))
    server_socker.listen()

    while True:
        client_socket, adress = server_socker.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(adress)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
