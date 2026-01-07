# Pergunte ao usuário sua idade
# Use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

def classificador(idade): 
    idade = int(idade)
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 < idade <= 18:
        return "Adolescente"
    elif 19 <= idade:
        return "Adulto"
    
def main():
    print("\nClassificador de Idade\n")
    print(classificador(input("Qual a sua idade? ")))

if __name__ == '__main__':
    main()