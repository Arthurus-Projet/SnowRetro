print('client')
import time
import socket

for pings in range(10000):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        client_socket.settimeout(1.0)
        message = b'test'
        message = bytes("vasi film mes couilles ", 'utf-8')
        addr = ("109.208.115.167", 8081)

        start = time.time()
        client_socket.sendto(message, addr)
        try:
            data, server = client_socket.recvfrom(40)
            end = time.time()
            elapsed = end - start
            print(f'{data} {pings} {elapsed}')
            client_socket.sendto(bytes("vasi film mes couilles", 'utf-8'), addr)
        except socket.timeout:
            print('REQUEST TIMED OUT')

    except:
        pass
