import matplotlib.pyplot as plt

horas_estudo = [1, 2, 3, 4, 5, 6, 7, 8]
nota_final = [6.5, 7.0, 7.8, 8.2, 5.8, 6.5, 6.9, 7.4]

plt.scatter(horas_estudo, nota_final, color="darkorange")
plt.title("Relação entre horas de estudo e nota final")
plt.xlabel("Horas de estudo por semana")
plt.ylabel("Nota final")
plt.grid(True)
plt.show()