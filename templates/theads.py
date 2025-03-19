'''
Template
Útil para: Executar várias tarefas ao mesmo tempo
'''
import threading
import time

def tarefa(nome, tempo):
    print(f"Iniciando {nome}...")
    time.sleep(tempo)
    print(f"Finalizando {nome}!")

def main():
    t1 = threading.Thread(target=tarefa, args=("Tarefa 1", 3))
    t2 = threading.Thread(target=tarefa, args=("Tarefa 2", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Todas as tarefas foram concluídas!")

if __name__ == "__main__":
    main()
