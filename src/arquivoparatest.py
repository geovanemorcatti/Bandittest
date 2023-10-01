# Exemplo de código com vulnerabilidade
import os

def execute_comando():
    comando = input("Digite um comando para ser executado: ")
    os.system(comando)

execute_comando()
