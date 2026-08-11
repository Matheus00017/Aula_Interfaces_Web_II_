n = int(input("Números: "))
div = 0

for i in range(1 , n+1):
    if n % i == 0:
        div += 1
if div == 2:
    print("Primo")
else:
    print("Não é primo")