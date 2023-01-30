import random


def jogar():

    print('*****************')
    print('**Jogo da forca**')
    print('*****************')

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    posicao = random.randrange(0, len(palavras))

    palavra_secreta = palavras[posicao].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você venceu")
    else:
        print("Perdeu otário")

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
