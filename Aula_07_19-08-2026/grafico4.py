import matplotlib.pyplot as plt

meses = ["jan", "Fev", "Mar", "Abr"]
matematica = [7.0, 8.0, 9.0, 5.0]
portugues = [6.5, 7.0, 7.2, 7.8]

figuras, eixos = plt.subplots(1, 2, figsize=(10, 4))

eixos[0].plot(meses, matematica, marker="o", color="royalblue")
eixos[0].set_title("Matemática")

eixos[1].plot(meses, portugues, marker="o", color="crimson")
eixos[1].set_title("Português")

plt.tight_layout()
plt.savefig("boletim.png")
plt.show()