def criar_conta(agencia, qtde_conta, cpf, contas):
    senha = input("Informe uma senha de 4 digitos: ")
    qtde_conta = qtde_conta + 1
    contas.append({"agencia":agencia, "conta" : qtde_conta, "cpf" : cpf, "senha" : senha})
    print("\n Conta Criada Com Sucesso")

def criarUsuario(usuarios):
    
    cpf = input("Digite o seu CPF: ")
    existe_usuario = filtrar_usuarios(cpf, usuarios)
    if existe_usuario:
        print("\n Já existe usuario com esse cpf")
        return ''
    else:    
        nome = input("Digite o seu nome completo: ")
        data_nascimento = input("Informe a sua data de nascimento: (dd-mm-aaaa) ")
        endereco = input("Informe o endereço completo: Rua, n°, Municipio/Estado ")
        usuarios.append({"nome":nome, "nasc" : data_nascimento, "cpf" : cpf, "endereco": endereco})
        return cpf

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuarios in usuarios if usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def verifica_login(cpf, contas, senha):
    contas_filtradas = [contas for contas in contas if contas["cpf"] == cpf]
    if contas_filtradas:
        if contas_filtradas[0]['senha'] == senha:
            return contas_filtradas[0] 
        else:
            return None

def extratoCompleto(extrato, saldo):
    if extrato == '':
        print("Ainda não há movimentações nesta conta. o saldo esta zerado")
        
    else:
        print("\n Inicio do Extrato")
        print("==================")
        print(extrato)    
        print("Fim do Extrato")

        print("\n")
        print("==================")
        print(f"Saldo {saldo:.2f}")


def depositar(saldo):
    deposito =  float(input( "Informe agora o valor a depósitar: "))
    if deposito > 0:
        saldo += deposito
        print(f"Ok, você depositou: R$ {deposito:.2f}\n")
        extrato = f"Deposito =+  R$ {deposito:.2f}\n"
        return extrato, saldo
    else:
        return ''
def sacar(limite_saques, saldo, limite):
        saque =  float(input( "Informe o valor do saque: "))
        if limite_saques < 3     :
            if saque > 0 and saque < limite:
                if saldo > saque :
                    saldo -= saque
                    print(f"Ok, você sacou: R$ {saque:.2f}\n")
                    extrato = f"Saque =-  R$ {saque:.2f}\n"
                    limite_saques += 1 
                    return extrato, saldo
                else :
                    print("Ops, Não há fundos suficientes")
                    return '', ''

            else :
                if saque > limite:
                    print("Saque não realizado pois o valor excedeu o limite maximo de R$500,00 por transação" )
                    return '', ''

                else :
                    print("Saque não realizado, verifique o valor e tente novamente" )
                    return '', ''

        else :  
            print("Limite de saques excedidos" )
            return '', ''


execute = True
extrato  = ''
saldo = 0
limite = 500
limite_saques = 0 
usuarios = []
contas = []
logado = 0
qtde_conta = 0 
agencia = '0001'
while execute:
    if(logado):
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
            logado = 0
            continue

        if escolha not in ('1', '2', '3'):
            print("Escolha inválida. Por favor, escolha uma opção válida.")
            continue

        if escolha == '1':
            extratoCompleto(extrato, saldo)
            continue
        
        if escolha == '2':  
            deposito, novo_saldo = depositar(saldo)
            extrato += deposito
            saldo = novo_saldo

        if escolha == '3':  
            saque, novo_saldo  = sacar(limite_saques, saldo, limite)
            if saque != '' :
                extrato += saque
                saldo = novo_saldo
    else:
        print("")
        print("")
        print("=========================")
        print("Escolha uma operação:")
        print("1. Cadastrar")
        print("2. Entrar")
        print("3. Sair")
        print("=========================")
        print("")
        escolha_login = input("Digite o número da operação: ")
        if escolha_login == '3':
            print("Ok, nos veremos na proxima")
            break

        if escolha_login not in ('1', '2', '3'):
            print("Escolha inválida. Por favor, escolha uma opção válida.")
            
        if escolha_login == '1':
            cpf = criarUsuario(usuarios)
            if cpf != '':
                criar_conta(agencia, qtde_conta, cpf, contas)
        
        if escolha_login == '2':
            cpf = input("Informe o seu cpf: ")
            senha = input("Informe uma senha de 4 digitos: ")
            conta = verifica_login(cpf, contas, senha)
            if conta is None:
                print("Conta não localizada")
            else:
                usuario = filtrar_usuarios(conta['cpf'], usuarios)
                print(f"Olá {usuario['nome']}, você esta logado ")
                logado = 1


