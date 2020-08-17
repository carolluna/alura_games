
import random

def primeira_mensagem():
    print ("*********************************")
    print ("***Bem vindo no jogo de Forca!***")
    print ("*********************************")

def lista_de_palavras():
    palavras = []
    with open('palavras.txt','r') as file:
        for line in file:
            palavras.append(line)
    return palavras

def escolher_palavras():
    palavras = lista_de_palavras()
    palavra_index = random.randrange(0,len(palavras))
    palavra_secreta = palavras[palavra_index].strip().lower()
    return palavra_secreta

def criar_result(palavra_secreta):
    result = ["_" for letra in palavra_secreta]
    return result

def pedir_chute():
    chute = input("Qual letra?")
    chute = chute.strip().lower()
    return chute

def chute_correto(palavra_secreta, chute, result):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            result[index] = letra
        index += 1
    return result

def enforcado():
    print("Você foi enforcado!!")

def ganhou_jogo():
    print("Parabéns, você acertou a palavra!!")


def jogar_forca():

    primeira_mensagem()
    palavra_secreta = escolher_palavras()
    result = criar_result(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(result)

    while(not enforcou and not acertou):
        chute = pedir_chute()

        if chute in palavra_secreta:
            result = chute_correto(palavra_secreta, chute, result)
        else: 
            erros += 1

        if erros == 6:
            enforcado()
            break         

        if '_' not in result:
            ganhou_jogo()
            break
            
        print(result)   

    print ("Fim de Jogo!")

if __name__ == "__main__":
    jogar_forca()