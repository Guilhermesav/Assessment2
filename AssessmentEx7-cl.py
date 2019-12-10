#Escreva um programa cliente e servidor sobre UDP em Python que:
#O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor e espera receber a resposta durante 5s.
#Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
#O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta.
import socket,pickle,time

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = 'ola, Favor enviar a quantidade de memoria total e disponivel no disco principal'
msg = msg.encode('ascii')
cliente = socket.gethostname()
ip = socket.gethostbyname(cliente)
terminou = False
soma = 0
while True:
    udp.sendto(msg,(ip, 9991))
    soma = soma + 1
    print(soma)
    (msg,servidor) = udp.recvfrom(4096)
    print(pickle.loads(msg))
    if soma == 5:
        print("Tempo limite excedido")
        udp.close()
        exit()
    time.sleep(1)

