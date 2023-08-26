def desloca_bits_direita(numero, deslocamento):
    numero_final = numero >> deslocamento
    return "{0:b}".format(numero_final)

def desloca_bits_esquerda(numero, deslocamento):
    numero_final = numero << deslocamento
    return "{0:b}".format(numero_final)

def negacao_bits(numero):
    return "{0:b}".format(~numero)

def e_bits(numero1, numero2):
    return "{0:b}".format(numero1&numero2)

def ou_exclusivo_bits(numero1, numero2):
    return "{0:b}".format(numero1^numero2)

def ou_bits(numero1, numero2):
    return "{0:b}".format(numero1|numero2)

msg = "\nMenu do Bitwise, escolha uma operação\n1 - Movimentar bits para a esquerda\n2 - Movimentar bits para a direita\n3 - Realizar a operação de negação\n4 - Realizar a operação E\n5 - Realizar a operação OU EXCLUSIVO\n6 - Realizar a operação OU\n7 - Sair\n"

print(msg)

opcao = input("Digite o valor da operação desejada: ")

while(opcao != "7"):
    valor1 = int(input("Digite um valor que deseja usar nas operações: "))
    valor2 = int(input("Digite outro valor que deseja usar nas operações: "))
    if opcao == "1":
        print(f"\nDeslocando {valor2} bits a esquerda", desloca_bits_esquerda(valor1, valor2))
    elif opcao == "2":
        print(f"\nDeslocando {valor2} bits a direita", desloca_bits_direita(valor1, valor2))
    elif opcao == "3":
        print(f"\nNegando o {valor1}", negacao_bits(valor1))
        print(f"\nNegando o {valor2}", negacao_bits(valor2))
    elif opcao == "4":
        print(f"\nOperação E entre {valor1} e {valor2}", e_bits(valor1, valor2))
    elif opcao == "5":
        print(f"\nOperação OU EXCLUSIVO entre {valor1} e {valor2}", ou_exclusivo_bits(valor1, valor2))
    elif opcao == "6":
        print(f"\nOperação OU entre {valor1} e {valor2}", ou_bits(valor1, valor2))

    print(msg)
    opcao = input("Digite o valor da operação desejada: ")

print("Obrigado por utilizar o operador Bitwise!!")