INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# fechar o programa
while True:
    user_input = input("Deseja fechar o programa? (y/n): ")
    if user_input.lower() == "y":
        exit()
    elif user_input.lower() == "n":
        print("O programa permanecerá aberto.")
    else:
        print("Entrada inválida. Por favor, insira 'y' para fechar ou 'n' para continuar.")
