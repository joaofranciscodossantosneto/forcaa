def jogar():
    print("*****************")
    print("***Bem vindo ao jogo da Forca***")
    print("*****************")

    palavra_secreta = "parquinho"

    letras_acertadas = ["_","_","_","_","_","_","_","_","_"]

    enforcou = False
    acertou = False


    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra:")
        chute = chute.strip()

        index = 0 
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                index = index +1

    print(letras_acertadas)



    print("Fim do jogo")

if(__name__== " __main__"):
    jogar()
