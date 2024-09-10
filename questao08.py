notas = []


for i in range(4):
    nota=float(input("Por favor digite a nota do aluno: "))
    notas.append(nota)

mediaNota = sum(notas) / len(notas)


if mediaNota >= 7:
        print("Aluno APROVADO")
    else:
        print("Aluno REPROVADO")

print("A média das notas é: ", mediaNota)