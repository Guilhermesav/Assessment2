#Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:
#Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela.
#Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt deve ser somado ao segundo elemento de b.txt, e assim sucessivamente.
#Caso um arquivo tenha mais elementos que o outro, os elementos que sobrarem do maior devem ser somados a zero.
A = open('a.txt','r')
B = open('b.txt','r')
texto_A = A.read()
texto_B = B.read()

lista_texto_A = texto_A.split(' ')
lista_texto_B = texto_B.split(' ')
lista_num_A = []
lista_num_B = []
for a in lista_texto_A:
    lista_num_A.append(int(a))
for b in lista_texto_B:
    lista_num_B.append(int(b))
    
print(lista_num_A)
print(lista_num_B)
    
lista_soma = []

for i in range(len(lista_num_B)):
    try:
        soma = lista_num_B[i] + lista_num_A[i]
        lista_soma.append(soma)
    except IndexError:
        soma = lista_num_B[i] + 0
        lista_soma.append(soma)
        
print(lista_soma)