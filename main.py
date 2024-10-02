from XboxController import XboxController

def menu():
    controle_player_1 = XboxController("preto","bluetooth","10x15cm","210g")

    while True:
        print("Selecione a opção desejada:")
        print("1. Ligar Xbox\n2. Desligar Xbox\n3. Abrir Painel")

        escolha = int(input(""))

        if escolha == 1:
            controle_player_1.ligarXbox()
        elif escolha == 2:
            controle_player_1.desligarXbox()
            break
        elif escolha == 3:
            controle_player_1.abrirPainel()
        else:
            print("Opção inválida!")

menu()