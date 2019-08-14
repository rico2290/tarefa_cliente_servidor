import socket
import sys, time

# Criar Cliente UDP 
class ClienteUDP():

    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
        # return super().__init__(*args, **kwargs)
        self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def enviar_e_receber(self):
        enderecoDoServidor = (self.localhost, self.porta)
        mensagem = input('Digite mensagem a  enviar: ').encode()

        try:
            # Enviar mensagem
            print('Enviando {} ...'.format(mensagem))
            self.socket_UDP.sendto(mensagem, enderecoDoServidor)
            # Receber mensagem
            print('Aguradando mensagem...')
            dado , enderecoDoCliente = self.socket_UDP.recvfrom(4096)
            if dado:
                print('Mensagem {} do servidor: {}' .format(dado, enderecoDoCliente))

        finally:
            print ('Fechando conexão...')
            time.sleep(5)
            self.socket_UDP.close()

cliente_udp = ClienteUDP('localhost', 9890)
cliente_udp.enviar_e_receber()