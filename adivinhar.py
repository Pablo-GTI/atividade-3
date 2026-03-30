import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Adivinhe o número (1 a 100): "))
    
    if palpite == numero_secreto:
        print("Acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")