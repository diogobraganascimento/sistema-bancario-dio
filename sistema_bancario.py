menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("################ V. 1.4 ################")

while True:
    opcao = input(menu)
    valor = 0

    if opcao == "1":
        valor = float(input("Valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depositou: R${valor:.2f}\n"
        else:
            print("Operação inválida! Valor informado é inválido.")
    elif opcao == "2":
        valor = float(input("Valor a ser sacado: R$"))
        if valor > 0:
            if valor <=saldo:
                if numero_saques < LIMITE_SAQUES and valor <= limite:
                    saldo -= valor
                    extrato += f"Sacou: R${valor:.2f}\n"
                    numero_saques += 1
                elif LIMITE_SAQUES == numero_saques:
                    print("Você atingiu o limite de saques diários. Tente novamente amanhã.")
                elif valor > limite:
                    print("Valor solicitado é maior do que o permitido de R$500.")
            else:
                print("Não é possível sacar o dinheiro por falta de saldo.")
        else:
            print("Operação inválida! Valor informado é inválido.")
    elif opcao == "3":
        print("############ EXTRATO ############\n")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo em conta: R${saldo:.2f}")
        print("#################################")
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
