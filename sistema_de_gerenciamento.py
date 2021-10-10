lista  = []

def encontrar(elemento):
    retorno = 0
    TamanhoLista = len(lista)

    for i in range(0,TamanhoLista): # procurar em todas as listas internas
        if elemento in lista[i]:
            print("╔═══════════════════════════════════╗")
            print(f" Nome: {lista[i][0]}. \n Email:{lista[i][1]}")
            print("╚═══════════════════════════════════╝")
            retorno = elemento
    return (retorno)


def exibir():
    TamanhoLista = len(lista)
    print("╔═══════════════════════════════════╗")
    for i in range(0,TamanhoLista): # procurar em todas as listas internas
        print(f" Nome: {lista[i][0]} / Email:{lista[i][1]}")
    print("╚═══════════════════════════════════╝")


def EmOrdemAlfa():
    TamanhoLista = len(lista)
    listaAlfa = lista.copy()
    listaAlfa.sort()
    print("╔═══════════════════════════════════╗")
    for i in range(0,TamanhoLista): # procurar em todas as listas internas
        print(f" Nome: {listaAlfa[i][0]} / Email:{listaAlfa[i][1]}")
    print("╚═══════════════════════════════════╝")


def apagar(elemento):
    TamanhoLista = len(lista)

    for i in range(0,TamanhoLista): # procurar em todas as listas internas
        if elemento in lista[i]:
            print("╔═══════════════════════════════════╗")
            print("  Dados que seram deletados: ")
            print(f" Nome: {lista[i][0]} \n Email:{lista[i][1]}")
            print("╚═══════════════════════════════════╝")
            confirma = str(input("Confirme o delete com S ou N:")).upper()
            if confirma == 'S':
                del(lista[i])
                print("╔═════════════════════════════╗")
                print(" Dados deletados com sucesso! ")
                print("╚═════════════════════════════╝")
                return
            elif confirma == 'N':
                print("╔════════════════════════════╗")
                print("     Operação cancelada!      ")
                print("╚════════════════════════════╝")
                return
        else:
            print("╔═════════════════════════════╗")
            print("    Email não encontrado!      ")
            print("╚═════════════════════════════╝")
            return


def Alterar(elemento):
    TamanhoLista = len(lista)

    for i in range(0,TamanhoLista): # procurar em todas as listas internas
        if elemento in lista[i]:
            print("╔═══════════════════════════════════╗")
            print("  Dados que seram alterados: ")
            print(f" Nome: {lista[i][0]} \n Email:{lista[i][1]}")
            print("╚═══════════════════════════════════╝")
            
            NomeNovo = str(input(f"Informe o nome do novo:"))
            lista[i][0] = NomeNovo
            print("╔═════════════════════════════╗")
            print("  Nome alterado com sucesso!   ")
            print("╚═════════════════════════════╝")
            return
        else:
            print("╔═════════════════════════════╗")
            print("    Email não encontrado!      ")
            print("╚═════════════════════════════╝")
            return


SistemaGeral = True
while SistemaGeral:
    print("╔════════════════════════════════════════╗\n"
          "|                Sistema                 |\n"
          "| Opções:                                |\n"
          "| 1- Cadastrar novos usuários.           |\n"
          "| 2- Exibir usuários em ordem cadastrada.|\n"
          "| 3- Exibir usuários em ordem alfabética.|\n"
          "| 4- Verificar usuário por nome.         |\n"
          "| 5- Remover usuário por email.          |\n"
          "| 6- Alterar nome do usuário por email.  |\n"
          "| 7- Desligar sistema.                   |\n"
          "|                                        |\n"
          "╚════════════════════════════════════════╝\n")

    escolha = int(input(f"Escolha a opção desejada: "))

    if escolha == 1:
        SistemaCadastro = True
        while SistemaCadastro == True:
            Nomenovo = str(input(f"Informe o nome do novo usuário:"))
            Emailnovo = str(input(f"Informe o email do usuário {Nomenovo}: "))

            novoDado = []
            novoDado.append(Nomenovo)
            novoDado.append(Emailnovo)
            lista.append(novoDado)

            print("╔═══════════════════════════╗")
            print(f"    Dados inseridos:\n"
                    f" Nome:{Nomenovo} \n"
                    f" Email:{Emailnovo}")
            print("╚═══════════════════════════╝")

            repetir = True
            while repetir == True:
                continuar = str(input(f"Deseja cadastrar um novo usuário? S ou N?\n")).upper()
                if continuar == 'S':
                    SistemaCadastro = True
                    repetir = False
                    break
                elif continuar == 'N':
                    repetir = False
                    SistemaCadastro = False
                    break
                else:
                    repetir = True
           
            
    elif escolha == 2:
        exibir()

    elif escolha == 3:
        EmOrdemAlfa()

    elif escolha == 4:
        busca = str(input(f"Informe o nome do usuário que deseja encontrar: "))
        resp = encontrar(busca)
        if resp == 0:
            print("╔═══════════════════════════════╗")
            print(f" Usuário {busca}, não encontrado!")
            print("╚═══════════════════════════════╝") 
    elif escolha == 5:
        busca = str(input(f"Informe o email do usuário que deseja apagar: "))
        apagar(busca)

    elif escolha == 6:
        busca = str(input(f"Informe o email do usuário que deseja alterar: "))
        Alterar(busca)

    elif escolha == 7:
        SistemaGeral = True
        break

    else:
        print("Valor inválido!!!")
        SistemaCadastro = True