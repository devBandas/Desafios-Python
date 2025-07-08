import random
numero = (random.randint(1, 50))
adivinho = 0
while adivinho != numero :
    adivinho_str = input("Tente adivinhar o número de 1 a 50! ")
    if not adivinho_str.isdigit():
        print("Coloque um número")
        continue
    adivinho = int(adivinho_str)
    if adivinho > 50 :
        print("Coloque um número que seja no máximo 50")
        continue
    elif adivinho < 1 :
        print("Coloque um número que seja no mínimo 1")        
        continue
    
    if adivinho < numero :
        print("Tente mais alto")
    elif adivinho > numero :
            print("Tente menor")
else :
                print("Você Acertou!!!")
