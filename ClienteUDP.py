import socket, sys, os, time


# Criar Cliente UDP 
class ClienteUDP():

    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
        
        
        #self.socket_UDP.settimeout(2.0)
    def enviar_e_receber(self):
        time.sleep(3)
        enderecoDoServidor = (self.localhost, self.porta)
        mensagem = b'oi servidor'#.encode()
        fechar =  b'CLOSE'
        uptime  = b'UPTIME'  
        reqnum = b'REQNUM'      
        #conexao = True
        #while conexao:
        try:
            self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            print('Enviando mensagem: {} ...'.format(mensagem))
            self.socket_UDP.sendto(mensagem, enderecoDoServidor)
            # Receber mensagem
            #print('Aguradando mensagem...')
            dado , enderecoDoServidor = self.socket_UDP.recvfrom(2048)
            print(' chegando: {} do {}...'.format(dado, enderecoDoServidor))
            time.sleep(10)
            #tempo de execução de servidor
            self.socket_UDP1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print('Enviando mensagem: {} ...'.format(uptime))
            self.socket_UDP1.sendto(uptime, enderecoDoServidor)
            time.sleep(10)

            self.socket_UDP3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print('Enviando mensagem: {} ...'.format(reqnum))
            self.socket_UDP3.sendto(reqnum, enderecoDoServidor)
            time.sleep(10)            
            #fechar conexao
            self.socket_UDP2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print('Enviando mensagem: {} ...'.format(fechar))
            self.socket_UDP2.sendto(fechar, enderecoDoServidor) 
            time.sleep(2)               

            # if dado:
            #     print('Mensagem: {} do servidor: {}' .format(dado, enderecoDoServidor))
            # #conexao = False
            
        except:
            print( 'Nao foi possivel comunicar com o servior')
            #self.socket_UDP.accept()

    def fechar_conexao(self):
        os.system('cls')
        self.socket_UDP.close()        

cliente_udp1 = ClienteUDP('localhost', 5100)
cliente_udp1.enviar_e_receber()

