print('Client Jhony Blizard')
import time
import socket
from fonctions_reseau import *

# UDP Pas de garantie de livraison, mais très rapide — idéal pour les jeux


addr = ("176.140.159.32", 8080) # Mon Ipv4


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(0.5)

for pings in range(1_000_000):

    try:
        #client_socket.settimeout(1.0)

        start = time.time()
        message = lire_str('perso.txt')

        client_socket.sendto(message, addr)

        data, server = client_socket.recvfrom(1024)

        ecrire("enemi.txt", data.decode("utf-8"))
        print(f'{data} {pings}')
    except socket.timeout:
        print("Time out")
        continue
