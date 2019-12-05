#Escreva um programa em Python que:
#gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco.
#Obtenha o nome do diretório do usuário.
#Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
#gere um arquivo texto com os valores desta estrutura ordenados.
import psutil,os

diretorio = input()
os.chdir(diretorio)
lista_dir = os.listdir(diretorio)
arquivo_tamanho = {}
for i in lista_dir:
    informacoes = os.stat(i)
    tamanho = informacoes.st_size
    arquivo_tamanho[i] = os.stat(i).st_size

print(arquivo_tamanho)
   