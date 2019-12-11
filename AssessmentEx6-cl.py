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

"""import socket
import psutil, pickle
import os


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

while True:
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))
msg = socket_cliente.recv(1024)
nome_dir = msg.decode('ascii')
if os.path.isdir(nome_dir):
arquivos = os.listdir(nome_dir) socket_cliente.send(arquivos.encode('ascii'))
else:
print("Não encontrou o diretorio")
socket_cliente.send('-1'.encode('ascii'))

socket_cliente.close()"""
