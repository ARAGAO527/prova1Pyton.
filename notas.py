#--Refatoração de Média--#
soma_notas = 0

for i in range(1, 4):
    nota = float(input(f"Digite a nota do {i}º bimestre: "))
    soma_notas += nota

media = soma_notas / 3

print(f"Média final: {media:.2f}")