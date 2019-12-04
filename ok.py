import threading, time,multiprocessing
lista_tamanhos = [1000, 2000, 3000, 4000, 5000]
if __name__ == '__main__':
    
    for tam in lista_tamanhos:
        lista = [1.3, 10.4, 40.0, 59.87, 33.01, 101.4]*tam
        tamanho = len(lista)

        def calcPorcent(lista, inicio, fim):
            for i in range(inicio, fim):
                lista[i] = lista[i] * 0.1
        
       
        # Captura tempo inicial
        t_inicio = float(time.time())

        Nthreads = 3 # Número de threads a ser criado
     
        lista_threads = []
     

        
        for i in range(Nthreads):
            ini = i * tamanho//Nthreads # início do intervalo da lista
            fim = (i + 1) * tamanho//Nthreads # fim do intervalo da lista
            t = threading.Thread(target=calcPorcent, args=(lista, ini, fim))
            t.start() # inicia thread
            lista_threads.append(t)

             lista_process.append(p)
            
            
        for t in lista_threads:
            t.join() # Espera as threads terminarem
            
        # Captura tempo final
        t_fim = float(time.time())
        t_inicio_seq = float(time.time())
        
        for i in range(tamanho):
            lista[i] = lista[i] * 0.1

        t_fim_seq = float(time.time())

        print(f"Tempo total Paralelo em segundos, com {tam} Threads: {round(t_fim - t_inicio,15)}")
        print(f"Tempo total Sequencial em segundos: {round(t_fim_seq - t_inicio_seq,15)}")


