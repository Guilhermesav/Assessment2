#Escreva 3 programas em Python que resolva o seguinte problema:
#Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.
#sequencialmente (sem concorrência);
#usando o módulo threading com 4 threads;
#usando o módulo multiprocessing com 4 processos.
import multiprocessing, time, random,threading
def fatorial(n):
    fat = n
    for i in range(n-1,1,-1,):
        fat = fat * i
    return(fat)
def Fathread(lista,inicio,fim):
    resultados_t = []
    for i in range(inicio,fim):
        resultados_t.append(fatorial(lista[i]))
    return print(resultados_t)
def fatProc(q1, q2):
    result_proc = q1.get()
    saidas_p = []
    for i in range(len(result_proc)):
        fatorial(result_proc[i])
        saidas_p.append(fatorial(result_proc[i]))
    q2.put(result_proc)
    return print(saidas_p)
    
if __name__ == "__main__":
    entradas = [1,5,2,3,7,2,9,8]
    print('Sequencial')
    saidas = []
    t_seq_ini = float(time.time())
    for i in entradas:
        resultado = fatorial(i)
        saidas.append(resultado)
    print(saidas)
    t_seq_fim = float(time.time())
    N = len(entradas)
    print('Threading')
    t_th_ini = float(time.time())
    saidas_t = []
    Nthreads = 4
    lista_threads =[]
    for i in range(Nthreads):
        ini = i * N//Nthreads 
        fim = (i + 1) * N//Nthreads 
        t = threading.Thread(target=Fathread, args=(entradas,ini,fim))
        t.start()
        
        lista_threads.append(t)
        
    for t in lista_threads:
        t.join()

    t_th_fim = float(time.time())

    print('Multiprocessing')
    t_mp_ini = float(time.time())
    NProc = 4
    
    q_entrada = multiprocessing.Queue()
  
  
    q_saida = multiprocessing.Queue()
    lista_proc = []
    
    for i in range(NProc):
        ini = i * int(N/NProc) 
        fim = (i + 1) * int(N/NProc) 
        q_entrada.put(entradas[ini:fim])
        p = multiprocessing.Process(target=fatProc, args=(q_entrada,q_saida))
        p.start() 
        lista_proc.append(p)
        
    for p in lista_proc:
        p.join() 
    
    t_mp_fim = float(time.time())
    
    print("Tempo Sequencial:",(t_seq_fim - t_seq_ini))
    print("Tempo com threading:",(t_th_fim - t_th_ini))
    print("Tempo com multiprocessing:",(t_mp_fim - t_mp_ini))
    
