notas = [7.5, 8.0, 6.5, 9.0, 5.5]

soma = 0
for nota in notas:
    soma = soma + nota
    media = soma / len(notas)

print(f"Notas: {notas}")
print(f"Média da turma: {media: .2f}")