import random

def jogar():
    print("*****************")
    print("*** Bem-vindo ao jogo da Forca ***")
    print("*****************")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    print(palavras)

    aleatoria = random.randrange(0, len(palavras))
    palavra_secreta = palavras[aleatoria].upper()


    palavra_secreta = "parquinho"
    letras_acertadas = ["_" for letra in palavra_secreta] 

    enforcou = False
    acertou = False
    tentativas = 6  

    while not enforcou and not acertou:
        print("\nPalavra: ", " ".join(letras_acertadas))  
        print(f"Tentativas restantes: {tentativas}")
        chute = input("Digite uma letra: ").lower()

        if len(chute) != 1 or not chute.isalpha():  
            print("Por favor, digite apenas uma letra válida.")
            continue

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_acertadas[i] = chute
            print("Boa! Você acertou uma letra.")
        else:
            tentativas -= 1
            print("Letra incorreta!")

        if "_" not in letras_acertadas:
            acertou = True
            print(f"Parabéns! Você acertou a palavra: {''.join(letras_acertadas)}")

        if tentativas == 0:
            enforcou = True
            print(f"Você foi enforcado! A palavra era: {palavra_secreta}")

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()
