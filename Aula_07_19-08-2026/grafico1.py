import matplotlib.pyplot as plt

bimestres = [1,2,3,4]
turma_a = [6.5, 7.0, 7.8, 8.2]
turma_b = [5.8, 6.5, 6.9, 7.4]

plt.plot(bimestres, turma_a, marker="o", label="Turma A")
plt.plot(bimestres, turma_b, marker="o", label="Turma B")
plt.title("Evolução das médias por bimestre")
plt.xlabel("Bimestre")
plt.ylabel("Média")
plt.legend()
plt.grid("True")
plt.show()

