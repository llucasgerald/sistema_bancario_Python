menu = ("""= = =
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
= = =""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = float(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor a ser depositado"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += (f"deposito : R$ {valor_deposito:.2f}\n")
        else:
            print("Operacao falhou, valor informado invalido")

    elif opcao == 2:
        valor_saque = float(input("Digite o valor a ser sacado"))
        excedeu_saldo = (valor_saque > saldo)
        excedeu_limite = (valor_saque > limite)
        excedeu_saques = numero_saques > LIMITE_SAQUES
        if excedeu_saldo:
            print("Operacao falhou, voce nao tem saldo suficiente")
        elif excedeu_limite:
            print("Operacao falhou, o valor do saque excede o limite permitido")
        elif excedeu_saques:
            print("Operacao falhou, numero maximo de saques diario excedido")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += (f"Saque: R$ {valor_saque:.2f}\n")
        else:
            print("Operacao falhou, valor invalido")
    elif opcao == 3:
        print("\n=============== EXTRATO ===============")
        print("Nao foram realizadas operacoes" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
    elif opcao == 4:
        break
    else:
        print("opcao invalida, reinicie a operacao")