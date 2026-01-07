# Solicite ao usuário que insira um número. 
# Em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

def par_impar(numero):
    numero = int(numero)
    if numero / 2 == 0:
        return "Par!"
    else:
        return "ímpar!"
def main():
    print("Par ou Impar?\n\n")
    print(par_impar(input("Digite um número: ")))

if __name__ == '__main__':
    main()
