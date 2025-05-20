def jogar():
    print("*****************")
    print("***Bem vindo ao jogo da Forca***")
    print("*****************")

    palavra_secreta = "parquinho"
    enforcou = False
    acertou = False
    index = 0 


    while(not enforcou and not acertou):
        print("Jogando...")
        chute = input("Digite uma letra:")

        for letra in palavra_secreta:
            if(chute == letra):
                print(f"Encontrei a letra{letra} na posição {index}")
                index = index +1





                print("Fim do jogo")

                if(__name__== " __main__"):
                    jogar()