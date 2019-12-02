#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o programa do sistema Windows bloco de notas (notepad) para abrir o arquivo.
import psutil, time, os

nome_do_arquivo = input()
diretorio = os.listdir('.')
if os.path.isfile(nome_do_arquivo):
    