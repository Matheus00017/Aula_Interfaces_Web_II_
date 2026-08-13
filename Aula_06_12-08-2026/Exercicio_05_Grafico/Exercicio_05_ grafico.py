import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5]

temperaturas = [22, 24, 21, 26, 28]

plt.plot(dias, temperaturas)
plt.title("Temperatura ao longo da semana")
plt.xlabel("Dia")
plt.ylabel("Temperatura (°C)")
plt.show()