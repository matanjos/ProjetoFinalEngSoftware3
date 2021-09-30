def menu():                                                     #Definição da função MENU
    continuar=1                                                 #"continuar" é a variável responsável pelo inicio e fim do jogo.
    while continuar:                                            #Enquanto continuar tiver o valor 1, é exibido um menu de escolha até que um valor seja atribuido a variável.
        continuar = int(input("0. Sair \n"+
                              "1. Jogar novamente\n"))
        if continuar:                                           #Se a opção escolhida para "continuar" for igual a "1", chama a função "game".
            game()
        else:                                                   #Se a opção escolhida para "continuar" for igual a "0", finaliza a execução do jogo.
            print("Saindo...")

def game():                                                     #Definição da função "Game"
    jogada=0                                                    #Definição da variável jogada que contém o número de jogadas até o momento no jogo.

    while ganhou() == 0:                                        #Verifica o valor de ganhou e enquanto ganhou for igual a zero, ou seja, não houver ganhador, o jogo continua executando.
        print("\nJogador ", jogada%2 + 1)                       #Mostra qual jogador deve jogar nesta rodada de acordo com o numero de jogadas.
        exibe()                                                 #exibe o tabuleiro mais atual do jogo.
        linha  = int(input("\nLinha :"))                        #recebe o valor da linha que o jogador atual quer inserir sua jogada.
        coluna = int(input("Coluna:"))                          #recebe o valor da coluna que o jogador atual quer inserir sua jogada.

        if board[linha-1][coluna-1] == 0:                       #Se o local escolhido na matriz está desocupado, insere um simbolo.
            if(jogada%2+1)==1:                                      #Se for uma jogada impar, isere 1.
                board[linha-1][coluna-1]=1
            else:                                                   #se for uma jogada par, recebe -1.
                board[linha-1][coluna-1]=-1                     
        else:                                                   #Se não está vazio, mostra mensagem de erro e volta uma jogada.      
            print("Nao esta vazio")
            jogada -=1

        if ganhou():                                            #Verifica se ganhor sofreu alguma alteração com a ultima jogada, se sim, exibe o ganhador.
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas") 

        jogada +=1                                              #Incrementa jogada.
    
def ganhou():                                                   #Definição da função "Ganhou".
    for i in range(3):                                          #Verifica se alguém ganho nas linhas da matriz, e retorna o valor 1 para a função ganhou.
        soma = board[i][0]+board[i][1]+board[i][2]
        if soma==3 or soma ==-3:
            return 1
        
    for i in range(3):                                          #Verifica se alguém ganho nas colunas da matriz, e retorna o valor 1 para a função ganhou.
        soma = board[0][i]+board[1][i]+board[2][i]
        if soma==3 or soma ==-3:
            return 1
        
    diagonal1 = board[0][0]+board[1][1]+board[2][2]             #Define as diagonais da matriz.
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3: #Verifica se alguém ganho nas diagonais da matriz, e retorna o valor 1 para a função ganhou.
        return 1

    return 0                                                    #Se não houve nenhum ganhador na jogada retorna o valor 0.

def exibe():                                                    #Definição da função "Exibir".
    for i in range(3):                                          #Exibe os objetos do jogo de acordo com os valores da matriz.
        for j in range(3):
            if board[i][j] == 0:                                    #Se o valor é zero, deixa apenas um underline no local.
                print(" _ ", end=' ')
            elif board[i][j] == 1:                                  #Se o valor é 1, deixa um "X".
                print(" X ", end=' ')
            elif board[i][j] == -1:                                 #Se o valor é -1, deixa um "O".
                print(" O ", end=' ')

        print()
                

board= [ [0,0,0],                                               #Definição do Painel do JOGO.
         [0,0,0],
         [0,0,0] ]

menu()                                                          #Chama a função "menu" para iniciar o game.
