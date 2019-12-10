#Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso.
nome_do_arquivo = input()
arquivo = open(nome_do_arquivo,'r')
texto = arquivo.read()
texto_reverso = texto[::-1]
print(texto_reverso)



