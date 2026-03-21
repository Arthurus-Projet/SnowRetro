import random
import socket
from fonctions_reseau import *

print('Serveur Arthur Vision')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 8080)) # 0.0.0.0 = écoute sur toutes les interfaces (wifi, ethernet, localhost...)


while True:
    
    print("wait to receive")
    message, address = server_socket.recvfrom(2048)
    ecrire("enemi.txt", message.decode("utf-8"))
    print(f'{message}')



    message = lire_str('perso.txt')
    server_socket.sendto(message, address)
    print("Message Send")
