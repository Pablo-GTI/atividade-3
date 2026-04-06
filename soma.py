soma = 0

while True:
    numero = float(input("Digite um número (0 para parar): "))
    
    if numero != 0:
        soma += numero
    else:
        break

print("A soma total é:", soma)
