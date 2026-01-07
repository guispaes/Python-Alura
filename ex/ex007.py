# Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else 
# Para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
#
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

def cartesiano(x, y):
    """
    Recebe coordenadas x e y e retorna o quadrante do plano cartesiano
    ou indica se o ponto está no eixo ou na origem.
    """
    x, y = float(x), float(y)
    if x > 0 and y > 0:
        return "Primeiro Quadrante"
    elif x < 0 and y > 0:
        return "Segundo Quadrante"
    elif x < 0 and y < 0:
        return "Terceiro Quadrante"
    elif x > 0 and y < 0:
        return "Quarto Quadrante"
    else: 
        if x == 0 and y == 0:
            return "Origem"
        elif x == 0 or y == 0:
            return "Eixo"
def main():
    print("\nClassificador de Plano Cartesiano\n")
    resultado = cartesiano(input("Eixo X: "), input("Eixo Y: "))
    print(f"\n{resultado}")


if __name__ == '__main__':
    main()