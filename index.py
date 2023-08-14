
execute = True
extrato  = ''
saldo = 0
limite = 500
limite_saques = 0 
while execute:
    print("")
    print("")
    print("=========================")
    print("Escolha uma operação:")
    print("1. Extrato")
    print("2. Depositar")
    print("3. Saque")
    print("4. Sair")
    print("=========================")
    print("")
    escolha = input("Digite o número da operação: ")
    if escolha == '4':
        print("Ok, nos veremos na proxima")
        break

    if escolha not in ('1', '2', '3'):
        print("Escolha inválida. Por favor, escolha uma opção válida.")
        continue

    if escolha == '1':
        
        if extrato == '':
            print("Ainda não há movimentações nesta conta. o saldo esta zerado")
            continue
        else:
            print("\n Inicio do Extrato")
            print("==================")
            print(extrato)    
            print("Fim do Extrato")

            print("\n")
            print("==================")
            print(f"Saldo {saldo:.2f}")


            continue
    
    if escolha == '2':  
        deposito =  float(input( "Informe agora o valor a depósitar: "))
        if deposito > 0:
            saldo += deposito
            print(f"Ok, você depositou: R$ {deposito:.2f}\n")
            extrato += f"Deposito =+  R$ {deposito:.2f}\n"

    if escolha == '3':  
        saque =  float(input( "Informe o valor do saque: "))
        if limite_saques < 3 :
            if saque > 0 and saque < limite:
                if saldo > saque :
                    saldo -= saque
                    print(f"Ok, você sacou: R$ {saque:.2f}\n")
                    extrato += f"Saque =-  R$ {saque:.2f}\n"
                    limite_saques += 1 
                else :
                    print("Ops, Não há fundos suficientes")
            else :
                if saque > limite:
                    print("Saque não realizado pois o valor excedeu o limite maximo de R$500,00 por transação" )
                else :
                    print("Saque não realizado, verifique o valor e tente novamente" )
        else :  
            print("Limite de saques excedidos" )
        