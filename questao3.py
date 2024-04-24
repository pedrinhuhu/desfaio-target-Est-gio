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

# fechar o programa
while True:
    user_input = input("Deseja fechar o programa? (y/n): ")
    if user_input.lower() == "y":
        exit()
    elif user_input.lower() == "n":
        print("O programa permanecerá aberto.")
    else:
        print("Entrada inválida. Por favor, insira 'y' para fechar ou 'n' para continuar.")
