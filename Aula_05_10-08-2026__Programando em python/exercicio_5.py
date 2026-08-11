soma = 0
qtd = 0

nota = float(input("Digite uma nota (-1 para sair): "))

while nota != -1:
    soma += nota
    qtd += 1
    nota = float(input("Digite uma nota (-1 para sair): "))

if qtd == 0:
    print("Média = ", soma / qtd)
else:
    print("Nenhuma nota informada")
