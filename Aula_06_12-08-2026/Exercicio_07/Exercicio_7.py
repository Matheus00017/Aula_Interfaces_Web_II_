import matplotlib.pyplot as plt

categorias = ["Aprovados", "Recuperação", "Reprovados"]

quantidades = [18, 7, 3]

plt.pie(quantidades, labels=categorias, autopct="%1.1f%%")
plt.title("Situação da turma")
plt.show()