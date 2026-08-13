numero = int(input("Digite um número entre 1 e 10: "))

while numero <1 or numero >10:
    print(" Valor invalído, tente novamente. ")
    numero = int(input("Digite um numero entre 1 e 10 "))
print(f"Você digitou {numero}, valor válido! ")