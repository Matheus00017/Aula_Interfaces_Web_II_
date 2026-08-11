n = int (input("N: "))
cont = 0
for i in range(1, n+1):
    if i % 2 == 0:
        cont += 1

print ("Quantidade de pares =", cont)