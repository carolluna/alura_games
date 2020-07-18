import random

def jogar_adv():
    print ("*********************************")
    print ("Bem vindo no jogo de Adivinhação!")
    print ("*********************************")

    numero_secreto = random.randrange(1,101)
    nivel = 0
    pontos = 1000

    print ("Qual o nível de dificuldade?")
    while (nivel < 1 or nivel > 3):
        nivel = int(input("(1) Fácil, (2) Médio, (3) Difícil. \nEscolha o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5



    for rodada in range(tentativas):
        
        print (f"Tentativa {rodada+1} de {tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1) or (chute > 100):
            print ("Você deve digitar um número entre 1 e 100")
            continue

        if (numero_secreto == chute):
            print ("Você acertou!")
            break
        elif (numero_secreto < chute): 
            print ("Você errou!")
            print ("O seu chute é maior que o numero secreto!")
        else:
            print ("Voce errou!")
            print ("O seu chute é menor que o numero secreto!")
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
    print (f"Sua pontuação foi: {pontos}")
    print ("Fim de Jogo!")