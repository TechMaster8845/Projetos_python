'''
Template
Útil para: Scripts que executam tarefas repetitivas
'''

import os
import time

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def executar_tarefa():
    print("Executando tarefa...")
    time.sleep(2)  # Simula um tempo de processamento
    print("Tarefa concluída!")

def main():
    limpar_terminal()
    executar_tarefa()

if __name__ == "__main__":
    main()
