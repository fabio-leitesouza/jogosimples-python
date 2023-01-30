import random

def jogar():
  print('*****************')
  print('Jogo de adivinhar')
  print('*****************')
  
  valormax = 1001
  numero_secreto = random.randrange(1, valormax)
  tentativas = 0
  pontos = 10000
  
  print("Qual o nível de dificuldade?")
  print("(1)-Fácil (2)-Médio (3)Difícil")
  
  nivel = int(input("Defina a dificuldade: "))
  if (nivel == 1):
      tentativas = 20
  elif (nivel == 2):
      tentativas = 10
  else:
      tentativas = 5
  
  for rodada in range(1, tentativas + 1):
  
      print("Tentativa {} de {}".format(rodada, tentativas), "\n")
      chute_str = input("Digite um número de 1 a 1000: ")
      print("Você chutou: ", chute_str)
      chute = int(chute_str)
      if (chute < 1 or chute > 1000):
          print("Você precisa digitar um número entre 1 e 100")
          continue
      acertou = chute == numero_secreto
      maior = chute > numero_secreto
      menor = chute < numero_secreto
  
      if (acertou):
          print("Você acertou e fez {} pontos".format(pontos))
          break
      else:
          if (maior):
              print("Você chutou um número maior que o número secreto")
          elif (menor):
              print("Você chutou um número menor que o número secreto")
          pontos_perdidos = abs(numero_secreto - chute)
          pontos = pontos - pontos_perdidos
  
  print("Fim do jogo")

if(__name__=="__main__"):
  jogar()

   

