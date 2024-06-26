menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depositado valor de R$ {valor:.2f}")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor inválido. Por favor tente novamente")
    elif opcao == 2:
        valor = float(input("Insira o valor a ser sacado: "))
        if valor > saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print("Valor do saque excede o limite")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f} \n"
            print(f"Sacado valor de R$ {valor:.2f}")
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 3:
        if not extrato:
            print("Não foram relizadas movimentações na conta.")
        else:
            print("Extrato".center(20, "=") + "\n")
            print(extrato)
            print("".center(20, "="))
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Por favor tente novamente")