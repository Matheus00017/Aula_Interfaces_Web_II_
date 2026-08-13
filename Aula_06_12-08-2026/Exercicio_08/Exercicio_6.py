import matplotlib.pyplot as plt

numeros = list(range(1, 11))

quadrados = []

for n in numeros:
    quadrados.append(n ** 2)

plt.plot(numeros, quadrados, marker="o")
plt.title("Numeros X seus quadrados")
plt.xlabel("Números")
plt.ylabel("Quadrados")
plt.grid(True)
plt.show()