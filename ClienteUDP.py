import socket, sys, os, time


# Criar Cliente UDP 
class ClienteUDP():

    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta

    def enviar_e_receber(self):
        time.sleep(3)
        enderecoDoServidor = (self.localhost, self.porta)
        conexao = True
        
        try:
            self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while conexao:
                msn = (input('digite a mensagem: '))
                msn = bytes(msn, 'utf-8')
                print('Enviando mensagem: {} ...'.format(msn))
                self.socket_UDP.sendto(msn, enderecoDoServidor)                
                if msn in [b'CLOSE', b'close']:
                    conexao = False
                    print('Fechando conexao com {} ...'.format(enderecoDoServidor))
                    time.sleep(5)
                    self.socket_UDP.close()
                    os.system('cls')
                dado , enderecoDoServidor = self.socket_UDP.recvfrom(2048)
                print('Mensagem: {} do servidor {}...'.format(dado, enderecoDoServidor))
        except:
            print( 'Nao foi possivel comunicar com o servior')
       
    

cliente_udp1 = ClienteUDP('localhost', 5100)
cliente_udp1.enviar_e_receber()

