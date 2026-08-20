import matplotlib.pyplot as plt

notas = [6.5, 7.0, 7.8, 8.2, 5.8, 6.5, 6.9, 7.4, 5.0, 6.8]

plt.hist(notas, bins=6, color="mediumseagreen", edgecolor="black")
plt.title("Distribuição das notas da turma")
plt.xlabel("Notas")
plt.ylabel("Quantidade de alunos")
plt.show()