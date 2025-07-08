import random
numero = (random.randint(1, 50))
adivinho = 0
while adivinho != numero :
    adivinho_str = input("Tente adivinhar o número de 1 a 50! ")
    if not adivinho_str.isdigit():
        print("Coloque um número")
        continue
    adivinho = int(adivinho_str)   
    if adivinho < numero :
        if adivinho > 50 :
             print("Coloque um número que seja no máximo 50.")
        elif adivinho < 1 :
             print("Coloque um número que seja no mínimo 1.")     
        else :
             print("Tente maior!")
    elif adivinho > numero :
        if adivinho > 50 :
             print("Coloque um número que seja no máximo 50.")
        elif adivinho < 1 :
             print("Coloque um número que seja no mínimo 1.")
        else :
             print("Tente menor!")
else :
        print("Você Acertou!!!")
