import multiprocessing, time, random,threading
def somaProc(q1, q2):
    listaproc = q1.get()
    for i in range(len(listaproc)):
        listaproc[i] = listaproc[i]*0.1
    q2.put(listaproc)
    
def calcPorcent(lista, inicio, fim):
    for i in range(inicio, fim):
        lista[i] = lista[i] * 0.1
                
if __name__ == "__main__":
    lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101.4]*100
    N = len(lista)
    t_inicio = float(time.time())
    
    NProc = 4
    
    q_entrada = multiprocessing.Queue()
  
  
    q_saida = multiprocessing.Queue()
    lista_proc = []
    
    for i in range(NProc):
        ini = i * int(N/NProc) 
        fim = (i + 1) * int(N/NProc) 
        q_entrada.put(lista[ini:fim])
        p = multiprocessing.Process(target=somaProc, args=(q_entrada,
        q_saida))
        p.start() 
        lista_proc.append(p)
        
        
    for p in lista_proc:
        p.join() 
    soma = []
    
    for i in range(0, NProc):
        soma.extend(q_saida.get())
 
    t_fim = float(time.time())
    
    
    
    t_thread_ini =  float(time.time())

    Nthreads = 3 
 
    lista_threads = []
 

    for i in range(Nthreads):
        ini = i * N//Nthreads 
        fim = (i + 1) * N//Nthreads 
        t = threading.Thread(target=calcPorcent, args=(lista, ini, fim))
        t.start() 
        lista_threads.append(t)

        
    for t in lista_threads:
        t.join()
        
    t_thread_fim = float(time.time())
    print("Soma:", soma)
    print("Tempo total:", t_fim - t_inicio,t_thread_fim-t_thread_ini)
    
