def verifica_fibonacci(numero):
    a, b = 0, 1
    
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    
    return False

def verificar_e_imprimir(numero):
    if verifica_fibonacci(numero):
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")

numeros_teste = [0, 1, 2, 9, 20]
for numero in numeros_teste:
    verificar_e_imprimir(numero)

# fechar o programa
while True:
    user_input = input("Deseja fechar o programa? (y/n): ")
    if user_input.lower() == "y":
        exit()
    elif user_input.lower() == "n":
        print("O programa permanecerá aberto.")
    else:
        print("Entrada inválida. Por favor, insira 'y' para fechar ou 'n' para continuar.")
