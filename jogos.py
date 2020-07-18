from jogo_adv import jogar_adv
from forca import jogar_forca

print ("*********************************")
print ("*******Escolha o seu jogo!*******")
print ("*********************************")

print ("Jodos disponíveis: \n(1) Adivinhação \n(2) Forca")

jogo = int(input("Entre com o número do jogo: "))

if jogo == 1:
    jogar_adv()
    
elif jogo == 2:
    jogar_forca()