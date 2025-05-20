def jogar():
    print("*****************")
    print("***Bem vindo ao jogo da Forca***")
    print("*****************")

    palavra_secreta = "parquinho"

    letras_acertadas = ["_","_","_","_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    index = 0 


    while(not enforcou and not acertou):
        print("Jogando...")
        chute = input("Digite uma letra:")

    index = 0 
    for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                index = index +1
    print(letras_acertadas)



    print("Fim do jogo")

    if(__name__== " __main__"):
     jogar()