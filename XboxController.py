class XboxController():
    def __init__(self,cor,tipoConexao,dimensao,peso):
        self.cor = cor
        self.tipoConexao = tipoConexao
        self.dimensao = dimensao
        self.peso = peso
        self.xboxLigado = False

    def pressiona_botao_acoes(self, qtdBotoes):
        self.qtdBotoes = qtdBotoes

        def a(self):
            self.corA = "Verde"
        def b(self):
            self.corB = "Vermelho"
        def x(self):
            self.corX = "Azul"
        def y(self):
            self.corY = "Amarelo"

    def ligarXbox(self):
        if self.xboxLigado == True:
            print("Xbox já está ligado.")
        else:
            self.xboxLigado = True
            print("Xbox ligado com sucesso.")

    def desligarXbox(self):
        if self.xboxLigado == True:
            self.xboxLigado = False
            print("Xbox desligado com sucesso.")
        else:
            print("Xbox já está desligado.")

    def abrirPainel(self):
        if self.xboxLigado == True:
            print("Painel aberto com sucesso.")
            
            while True:
                print("Escolha qual jogo deseja jogar:\na) Mortal Combat\nb) Minecraft Dungeons\nc) Fallout 4\nd) Sniper Elite\ne) Voltar")
                escolha = input("")

                if escolha == "a" or escolha == "A":
                    print("Você está jogando Mortal Combat.")
                    print("1. Parar de Jogar")
                    e = int(input(""))
                    if e == 1:
                        print("\n1. Sair sem salvar progresso\n2. Sair e salvar progresso ")            
                        g = int(input(""))
                        if g == 1:
                            print("Saindo...")
                            print("Jogo encerrado")
                        elif g == 2:
                            print("Salvando seu progresso...")
                            print("Jogo encerrado e progresso salvo com sucesso.")
                    else:
                        print("Opção inválida")
                                
                elif escolha == "b" or escolha == "B":
                    print("Você está jogando Minecraft Dungeons")
                    print("1. Parar de Jogar")
                    e = int(input(""))
                    if e == 1:
                        print("\n1. Sair sem salvar progresso\n2. Sair e salvar progresso ")            
                        g = int(input(""))
                        if g == 1:
                            print("Saindo...")
                            print("Jogo encerrado")
                        elif g == 2:
                            print("Salvando seu progresso...")
                            print("Jogo encerrado e progresso salvo com sucesso.")
                    else:
                        print("Opção inválida")

                elif escolha == "c" or escolha == "B":
                    print("Você está jogando Fallout 4")
                    print("1. Parar de Jogar")
                    e = int(input(""))
                    if e == 1:
                        print("\n1. Sair sem salvar progresso\n2. Sair e salvar progresso ")            
                        g = int(input(""))
                        if g == 1:
                            print("Saindo...")
                            print("Jogo encerrado")
                        elif g == 2:
                            print("Salvando seu progresso...")
                            print("Jogo encerrado e progresso salvo com sucesso.")
                    else:
                        print("Opção inválida")

                elif escolha == "d" or escolha == "D":
                    print("Você está jogando Sniper Elite")
                    print("1. Parar de Jogar")
                    e = int(input(""))
                    if e == 1:
                        print("\n1. Sair sem salvar progresso\n2. Sair e salvar progresso ")            
                        g = int(input(""))
                        if g == 1:
                            print("Saindo...")
                            print("Jogo encerrado")
                        elif g == 2:
                            print("Salvando seu progresso...")
                            print("Jogo encerrado e progresso salvo com sucesso.")
                    else:
                        print("Opção inválida")

                elif escolha == "e" or escolha == "E":
                    break
                else:
                    print("Opção inválida.")
        else:
            print("Para abrir o painel, você precisa primeiro ligar o xbox!")

    def voltar(self):
        pass

    def clicarBotaoA(self):
        pass

    def clicarBotaoB(self):
        pass

    def clicarBotaoX(self):
        pass

    def clicarBotaoY(self):
        pass
