#Escreva um programa em Python que:
#obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
#imprima o nome do processo e seu PID;
#imprima também o percentual de uso de CPU e de uso de memória.
import psutil,os,time,subprocess

while True:
    memoria = psutil.virtual_memory()
    mem_disp = memoria.total - memoria.available
    percentual_cpu = psutil.cpu_percent()
    print(percentual_cpu)
    try:
        for i in psutil.process_iter():
            processo = i.name()
            pid = i.pid
            print("Pid:",pid,"Nome:",processo)
    except psutil.NoSuchProcess:
        print("process terminated")
    print(percentual_cpu,"%")
    print(round(mem_disp/1024/1024/1024,2),"GB")
    time.sleep(2)
