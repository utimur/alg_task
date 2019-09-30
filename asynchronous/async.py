import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(('localhost',5001))
server_socket.listen()

while True:
    print('before accept')
    client_socket,addr = server_socket.accept()
    print('connection from', addr)

    while True:
        print('before recv')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'hello world\n\n'.encode()
            client_socket.send(response)
