#  Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
#  Utilize um bloco try-except para lidar com possíveis exceções.

lista = []
while True:
    try:
        lista.append(int(input("\nDigite um número para adicionar a lista: ")))
        continuar = str(input("\nQuer continuar adicionando números? S/N: ").strip().upper())
        if continuar == "S":
            pass
        elif continuar == "N": 
            print("\nParando de adicionar números! Vamos a soma: ")
            break
        else:
            print("\nPor favor, utilize uma op©ão válida. S ou N.")
    except:
        print("Digite um número válido.") 
    
soma = 0
try:
    for numero in lista:
        soma += numero
except:
    print("\nA lista está vazia!")

print(f"\nA soma dos números é igual a {soma}")