# Solicite ao usuário um número
# Em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

def tabuada(numero):
    print("-"*20)
    for m in range(1,11):
        print(f"{numero} x {m} = {numero*m}")
    print("-"*20)

def main():
    tabuada(int(input("Digite um número para ver sua tabuada: ")))

if __name__ == '__main__': 
    main()
    