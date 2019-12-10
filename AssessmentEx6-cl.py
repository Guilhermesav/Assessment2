#Escreva um programa cliente e servidor sobre TCP em Python em que:
#O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
#O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta.
import socket, sys, os
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_dir = input('Entre com o nome do diretorio: ')
try:
    s.connect((socket.gethostname(), 8882))
    s.send(nome_dir.encode('ascii'))
    msg = s.recv(4096)
    mensagem = msg.decode('ascii')
    if mensagem == '-1':
        print("Diretorio não encontrado")
    else:
        print(mensagem)
except Exception as erro:
    print(str(erro))
s.close()
input("Pressione qualquer tecla para sair...")