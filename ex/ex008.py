# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

def soma_impar(inicio, fim):
    fim += 1
    soma = 0
    for i in range(inicio,fim):
        if i % 2 != 0:
            soma += i
        else:
            pass
    return soma

def main():
    print("Somador de números ímpares")
    print(f"A soma é: {soma_impar(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")))}")

if __name__ == '__main__':
    main()
