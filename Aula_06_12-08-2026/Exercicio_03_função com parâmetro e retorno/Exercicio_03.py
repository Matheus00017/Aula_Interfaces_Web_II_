def eh_primo(numero):
    if numero <2:
        return False
    for i in range(2, numero):
        if numero / i == 0:
            return False
    return True
num = int(input("Digite um número: "))

if eh_primo(num):
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")