import random
numero = (random.randint(1, 50))
adivinho = 0
while adivinho != numero :
    adivinho_str = input("Tente adivinhar o número de 1 a 50! ")
    if not adivinho_str.isdigit():
        print("MLK TU É MT BURRO É PRA POR NUMERO!")
        continue
    adivinho = int(adivinho_str)
    if adivinho > 50 :
        print("É ATÉ 50 VIADO")
        continue
    elif adivinho < 1 :
        print("É PELO MENOS 1 NE GAY")        
        continue
    
    if adivinho < numero :
        print("Tente mais alto")
    elif adivinho > numero :
            print("Tente menor")
else :
                print("Você Acertou!!!")
