# Função para realizar um deslocamento de bits para a direita
def desloca_bits_direita(numero, deslocamento):
    return numero >> deslocamento

# Função para realizar um deslocamento de bits para a esquerda
def desloca_bits_esquerda(numero, deslocamento):
    return numero << deslocamento

# Função para realizar a operação de negação de bits (bitwise NOT)
def not_bits(numero):
    return ~numero

# Função para realizar a operação E entre dois números (bitwise AND)
def and_bits(numero1, numero2):
    return numero1 & numero2

# Função para realizar a operação OU EXCLUSIVO entre dois números (bitwise XOR)
def xor_bits(numero1, numero2):
    return numero1 ^ numero2

# Função para realizar a operação OU entre dois números (bitwise OR)
def or_bits(numero1, numero2):
    return numero1 | numero2

# Função para converter um resultado em formato binário para string
def binario_para_string(resultado):
    return f"{resultado:b}"

# Função principal do programa
def main():
    msg = """
    Menu do Bitwise, escolha uma operação:
    1 - Movimentar bits para a esquerda
    2 - Movimentar bits para a direita
    3 - Realizar a operação NOT
    4 - Realizar a operação AND
    5 - Realizar a operação XOR
    6 - Realizar a operação OR
    7 - Sair
    """

    print(msg)

    # Loop principal do programa
    while True:
        opcao = input("Digite o valor da operação desejada: ")

        if opcao == "7":
            break

        if opcao not in ["1", "2", "3", "4", "5", "6"]:
            print("Opção inválida. Escolha uma opção válida.")
            continue

        valor_1 = int(input("Digite o primeiro valor que deseja utilizar na operação: "))
        valor_2 = int(input("Digite o segundo valor que deseja utilizar na operação: "))

        if opcao == "1":
            resultado = desloca_bits_esquerda(valor_1, valor_2)
            print(f"{valor_1} com {valor_2} bits deslocados para a esquerda: {binario_para_string(resultado)}")
        elif opcao == "2":
            resultado = desloca_bits_direita(valor_1, valor_2)
            print(f"{valor_1} com {valor_2} bits deslocados para a direita: {binario_para_string(resultado)}")
        elif opcao == "3":
            not_1 = not_bits(valor_1)
            not_2 = not_bits(valor_2)
            print(f"{valor_1} negado: {binario_para_string(not_1)}")
            print(f"{valor_2} negado: {binario_para_string(not_2)}")
        elif opcao == "4":
            resultado = and_bits(valor_1, valor_2)
            print(f"Operação AND entre {valor_1} e {valor_2}: {binario_para_string(resultado)}")
        elif opcao == "5":
            resultado = xor_bits(valor_1, valor_2)
            print(f"Operação XOR entre {valor_1} e {valor_2}: {binario_para_string(resultado)}")
        elif opcao == "6":
            resultado = or_bits(valor_1, valor_2)
            print(f"Operação OR entre {valor_1} e {valor_2}: {binario_para_string(resultado)}")

# Verifica se o programa está sendo executado diretamente
if __name__ == "__main__":
    main()

# Mensagem de agradecimento após a execução
print("Obrigado por utilizar o operador Bitwise!")
