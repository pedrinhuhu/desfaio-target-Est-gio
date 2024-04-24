
print("Primeira ida:")
print("Eu ligo o primeiro interruptor e o deixo ligado por alguns minutos.")
print("Em seguida, desligo o primeiro interruptor e ligo o segundo interruptor.")
print("Segunda ida")
print("Eu entro na sala das lâmpadas.")
print("A lâmpada que estiver acesa corresponde ao interruptor que eu liguei e desliguei uma vez (primeiro interruptor).")
print("A lâmpada que estiver apagada e ainda estiver fria corresponde ao interruptor que nunca foi ligado (terceiro interruptor).")
print("A lâmpada que estiver apagada, mas estiver quente, corresponde ao interruptor que eu liguei e permaneceu ligado por alguns minutos (segundo interruptor).")

# fechar o programa
while True:
    user_input = input("Deseja fechar o programa? (y/n): ")
    if user_input.lower() == "y":
        exit()
    elif user_input.lower() == "n":
        print("O programa permanecerá aberto.")
    else:
        print("Entrada inválida. Por favor, insira 'y' para fechar ou 'n' para continuar.")
