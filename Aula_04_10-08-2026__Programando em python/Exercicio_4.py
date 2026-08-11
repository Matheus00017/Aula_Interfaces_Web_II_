n = int(input("N: "))
fat = 1
i = 1

while i <= n:
    fat *= i
    i += 1

print("Fatorial =", fat)
