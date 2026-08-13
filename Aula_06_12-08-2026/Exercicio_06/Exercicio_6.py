import matplotlib.pyplot as plt

alunos = ["Matheus", "Riquelme", "Vitoria Huga" , "Lorran", "Nicolas"]

notas = [8.2, 9.4, 3.1, 6.6, 9.8]

plt.bar(alunos, notas, color="steelblue")
plt.title("Notas dos alunos")
plt.xlabel("Aluno")
plt.ylabel("Nota")
plt.show()