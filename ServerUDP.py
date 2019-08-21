import socket
import os, time, timeit

#Criar Servidor UDP 
class ServerUDP():

    def __init__(self, localhost, porta):
        self.localhost = localhost
        self.porta = porta
        self.tempo_inicio = timeit.default_timer()
        self.listaConexo = []
        
    def get_localhost_(self):
        return self.localhost

    def server_data(self):
        return ServerUDP.__dict__

    def get_porta_(self):
        return self.porta

    def get_default_localhost(self):
        try:
            host = socket.gethostname()
            print(socket.gethostbyname(host))
        except:
            print('Impossível pegar nome da máquina e localhost')


    # bind socket para porta 
    def enviar_e_receber(self):
        enderecoDoServidor = (self.localhost, self.porta)
        self.socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_UDP.bind(enderecoDoServidor)
        print('Aguradando mensagem... ')
        while True:
            
            mensagem, enderecoDoCliente = self.socket_UDP.recvfrom(2048)
            if mensagem:
                self.socket_UDP.sendto(mensagem, enderecoDoCliente)
                self.listaConexo.append(enderecoDoCliente[1])
                
                if mensagem == b'CLOSE':
                    # enviar = self.socket_UDP.sendto(mensagem, enderecoDoCliente)
                    # print('enviado {} para cliente {}'.format(mensagem, enderecoDoCliente))  
                    print('Fechando a comunicacao...')        
                    time.sleep(3)          
                    self.socket_UDP.close()
                    break
                if mensagem == b'UPTIME':
                    print( 'Tempo de execucao: {}'.format(timeit.default_timer() - self.tempo_inicio))
                if mensagem == b'REQNUM':
                    # if self.listaConexo is None:
                    #     print('Lista vazia')
                    print('Lista de conexoes: {}'.format(self.listaConexo))
                #print('Recebido {} do cliente {}'.format(mensagem, enderecoDoCliente))
                
                



servidor_udp = ServerUDP('localhost', 5100)
servidor_udp.enviar_e_receber()


