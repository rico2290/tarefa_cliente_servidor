import socket
import sys, os

#Criar Servidor UDP 
class ServerUDP():

    def __init__(self, ip, porta, localhost):
        self.ip = ip
        self.porta = porta
        self.localhost = localhost
        self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    
    def get_ip_(self):
        return self.ip

    def get_localhost_(self):
        print(self.localhost)
    
    def get_porta_(self):
        return self.porta

    def get_default_ip(self):
        try:
            host = socket.gethostname()
            print(socket.gethostbyname(host))
        except:
            print('Impossível pegar nome da máquina e ip')
    
    # bind socket para porta 
    def enviar_e_receber(self):
        #local = self.local
        # self.porta = porta
        enderecoDoServidor = (self.localhost, self.porta)
        self.socket_UDP.bind(enderecoDoServidor)
        while True:
            print('Aguradando mensagem...')
            mensagem, enderecoDoCliente = self.socket_UDP.recvfrom(4096)
            print('Recebido {} do cliente {}'.format(mensagem, enderecoDoCliente))
            if mensagem:
                enviar = self.socket_UDP.sendto(mensagem, enderecoDoCliente)
                print('enviado {} para cliente {}'.format(mensagem, enderecoDoCliente))

servidor_udp = ServerUDP('198.160.0.70', 9890, 'localhost')

servidor_udp.get_default_ip()
servidor_udp.enviar_e_receber()

