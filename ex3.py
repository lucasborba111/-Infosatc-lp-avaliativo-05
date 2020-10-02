for i in range(0,4):  
    nome = input("Nome(mínimo três letras):")
    while(len(nome)<3):
        print("O nome possui menos de tres letras")
        nome = input("Nome(mínimo três letras):")
    sobrenome = input("Sobrenome(mínimo três letras):")
    while(len(sobrenome)<3):
        print("O sobrenome possui menos de tres letras")
        sobrenome = input("Sobrenome(mínimo três letras):")
    endereco = input("Endereço:")
    senha = input("senha:")
    while((len(senha)<5) or (senha.isalnum()==True or senha.isalpha()==True)):
             senha = input("A senha precisa estar conforme os requisitos:")
    email = input("Escreva se email@email.com")
    for i in email:
        if("@" in email):
            break
    else:
        email = input("O email precisa de @")
    cliente={"nome:{}" .format(nome+" "+sobrenome),"Endereço:{}".format(endereco),"Senha:{}".format(senha),"Email:{}".format(email)}
    print(cliente)
    total=0
    total=total+1
    if(total==1):
        conta1={}
        conta1=cliente.copy()
        print("Sua conta foi definida com o nome: conta1")
    elif(total==2):
        conta2=cliente.copy()
        del cliente
        print("Sua conta foi definida com o nome: conta2")
    if(total==3):
        conta3=cliente.copy()
        print("Sua conta foi definida com o nome: conta3")
    elif(total==4):
        conta4=cliente.copy()
        print("Sua conta foi definida com o nome: conta4")
    saldoTotal=0
    depositar=0
    sacar=0
    def encerrarConta():
        if(total==1):           
           print(conta1)
           conta1.clear()
        elif(total==2):
           print(conta2)
           conta2.clear()
        if(total==3):
           conta3.clear()
           print(conta3)
        elif(total==4):
           conta4.clear()
           print(conta4)
    encerrarConta()
      
    def menu():  
        saldoTotal=0
        for i in range(0,4):                       
            menu = int(input("Opções do menu:\n1-Depositar\n2-Sacar\n3-Conferir Saldo\n4-Transferir\n5-Encerrar Conta")) 
            if(menu==1):
                depositar=float(input("Deposite uma quantia:"))
                saldoTotal=saldoTotal+depositar
                print("Saldo:",saldoTotal)
                while(depositar<0):
                     depositar=float(input("Deposite um saldo positivo:"))
                     if(depositar>=0):
                        saldoTotal=saldoTotal+depositar
                        print("Saldo:",saldoTotal)
                     else:
                         pass
            elif(menu==2):
                sacar=float(input("Saque um saldo"))
                saldoTotal=saldoTotal-sacar
                while(sacar>saldoTotal):
                      sacar=float(input("Saldo insuficiente, digite um saldo real"))
                      saldoTotal=saldoTotal-sacar
            elif(menu==3):
                       print("Seu saldo:",saldoTotal)
            elif(menu==4):
                    transferir = float(input("Transfira um saldo:"))
                    saldoTotal=saldoTotal-transferir
            elif(menu==5):
                     encerrar=input("Realmente deseja encerrar?")
                     if(encerrar=="sim"):
                         encerrarConta()
                     else:
                         pass
            else:
                 pass

    menu() 
   

    

