import forca
import adivinhacao

def jogo():
  print("***Escolha o jogo***")
  
  print("(1)-jogo de adivinha (2)-jogo da forca")
  jogo = int(input("Escolha o jogo: "))
  
  if (jogo == 1):
    print("Jogo de adivinhar")
    adivinhacao.jogar()
  if (jogo == 2):
    print("Jogo da forca")
    forca.jogar()

if(__name__=="__main__"):
  jogo()
  
  
