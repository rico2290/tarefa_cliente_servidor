import socket, sys, os, time


# Criar Cliente UDP 
class ClienteUDP():

    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
        # return super().__init__(*args, **kwargs)
        
        #self.socket_UDP.settimeout(2.0)
    def enviar_e_receber(self):
        enderecoDoServidor = (self.localhost, self.porta)
        mensagem = 'oi servidor '#.encode()
        conexao = True
        #while conexao:
        try:
            self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Enviar mensagem
            print('Enviando mensagem: {} ...'.format(mensagem))
            self.socket_UDP.sendto(mensagem, enderecoDoServidor)
            # Receber mensagem
            print('Aguradando mensagem...')
            dado , enderecoDoServidor = self.socket_UDP.recvfrom(2048)
            #print(dado)
            if dado:
                print('Mensagem: {} do servidor: {}' .format(dado, enderecoDoServidor))
            conexao = False
            print(dado)
        except:
            print( 'Nao foi possivel comunicar com o servior')
            #self.socket_UDP.accept()

    def fechar_conexao(self):
        os.system('cls')
        self.socket_UDP.close()        
        # fechar = print(input('Digite o comando [close]  pra fechar: '))
        # fechar.upper()
        # if fechar == 'CLOSE':
        #     os.system('cls')
        #     self.socket_UDP.close()
        # else:
        #     print('ops! vc digitou o comando errado')
#192.168.0.1
cliente_udp1 = ClienteUDP('localhost', 6010)
cliente_udp1.enviar_e_receber()
time.sleep(10)
'''

time.sleep(20)
cliente_udp2 = ClienteUDP('localhost', 8010)
cliente_udp2.enviar_e_receber()
time.sleep(10)
cliente_udp2.fechar_conexao()
'''