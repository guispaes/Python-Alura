from os import system
from time import sleep

restaurantes = []
def titulo():
    print("""                                                        
 _____     _              _____                         
|   __|___| |_ ___ ___   |   __|_ _ ___ ___ ___ ___ ___ 
|__   | .'| . | . |  _|  |   __|_'_| . |  _| -_|_ -|_ -|
|_____|__,|___|___|_|    |_____|_,_|  _|_| |___|___|___|
                                   |_|                  
    """)
def exibir_menu():
    resposta = int(input("\nDigite o índice da a©ão desejada:\n 1- Cadastar novo restaurante. \n 2- Listar restaurantes. \n 3- Ativar restaurante. \n 4- Sair. \n\nDigite sua resposta: "))
    return resposta
def cadastro():
    print("\nCadastro:")
    while True:
        restaurantes.append({'Nome do Restaurante': str(input("Nome: ").capitalize()),
                            'Categoria': str(input('Categoria: ').capitalize()),
                            'Status': False })
        continuar = str(input("\nQuer continuar adicionar outros estabelecimentos? S/N: ").strip().upper())
        if continuar == "S":
            pass
        elif continuar == "N": 
            print("\nVoltando ao menu.")
            break
def lista_restaurantes_ativos():
    print("\nLista de restaurantes ativos:")
    for restaurante in restaurantes:
        print(f"- {restaurante['Nome do Restaurante']} | {restaurante['Categoria']} | {restaurante['Status']}")
def ativar_restaurante():
    print("\nAtivar restaurante:")
def finalizar():
    print("\nFinalizando o programa.")
    sleep(1.5)
    system("clear")
    print("\nPrograma finalizado.")       

def main(): 
    titulo()
    while True:
        try:
            usuario = exibir_menu()
            if usuario == 1:
                cadastro()
            elif usuario == 2:
                lista_restaurantes_ativos()
            elif usuario == 3:
                ativar_restaurante()
            elif usuario == 4:
                finalizar()
                break
            else:
                print("\nPor favor, utilize uma op©ão válida.")
        except:
            print("\nPor favor, utilize uma op©ão válida.")


if __name__ == '__main__':
    main()