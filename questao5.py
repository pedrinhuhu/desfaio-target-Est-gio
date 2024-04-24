def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

def main():
    string_original = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(string_original)
    print("String original:", string_original)
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()

# fechar o programa
while True:
    user_input = input("Deseja fechar o programa? (y/n): ")
    if user_input.lower() == "y":
        exit()
    elif user_input.lower() == "n":
        print("O programa permanecerá aberto.")
    else:
        print("Entrada inválida. Por favor, insira 'y' para fechar ou 'n' para continuar.")