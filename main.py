from os import system
from time import sleep

def finalizar():
    sleep(1.5)
    system("clear")
    print("\nPrograma finalizado.")       

print("""                                                        
 _____     _              _____                         
|   __|___| |_ ___ ___   |   __|_ _ ___ ___ ___ ___ ___ 
|__   | .'| . | . |  _|  |   __|_'_| . |  _| -_|_ -|_ -|
|_____|__,|___|___|_|    |_____|_,_|  _|_| |___|___|___|
                                   |_|                  
    """)

while True:
    resposta_usuario = int(input("\nDigite o índice da a©ão desejada:\n 1- Cadastar novo restaurante. \n 2- Listar restaurantes. \n 3- Ativar restaurante. \n 4- Sair. \n\nDigite sua resposta: "))
    if resposta_usuario == 1:
        print("\nCadastro:")
    elif resposta_usuario == 2:
        print("\nLista de restaurantes ativos:")
    elif resposta_usuario == 3:
        print("\nAtivar restaurante:")
    elif resposta_usuario == 4:
        print("\nFinalizando o programa.")
        break
    else:
        print("\nPor favor, utilize uma op©ão válida.")

finalizar()
