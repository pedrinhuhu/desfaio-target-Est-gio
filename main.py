#questão 1

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

print("\n")

#questão 2

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

print("\n")
#questão 3

# Sequência a)
sequencia_a = [1, 3, 5, 7]
proximo_numero_a = sequencia_a[-1] + 2
sequencia_a.append(proximo_numero_a)
print(sequencia_a)
print("\n")
# Sequência b)
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_numero_b = sequencia_b[-1] * 2
sequencia_b.append(proximo_numero_b)
print(sequencia_b)
print("\n")
# Sequência c)
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_numero_c = sequencia_c[-1] + 13
sequencia_c.append(proximo_numero_c)
print(sequencia_c)
print("\n")
# Sequência d)
sequencia_d = [4, 16, 36, 64]
proximo_numero_d = sequencia_d[-1] + 36
sequencia_d.append(proximo_numero_d)
print(sequencia_d)
print("\n")
# Sequência e)
sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_numero_e = sequencia_e[-1] + sequencia_e[-2]
sequencia_e.append(proximo_numero_e)
print(sequencia_e)
print("\n")
# Sequência f)
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_numero_f = sequencia_f[-1] + 1
sequencia_f.append(proximo_numero_f)
print(sequencia_f)
print("\n")

#questão 4

def descobrir_interruptores():
    print("Ligando o primeiro interruptor")
    print("Aguarde alguns minutos")
    print("Desligando o primeiro interruptor e ligando o segundo interruptor")
    print("Aguarde alguns minutos")

descobrir_interruptores()

print("\n")
#questão 5

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
