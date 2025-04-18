# Dada uma lista contendo as notas de alunos em uma disciplina,
# escreva uma expressão para:
# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] 
# a) Encontrar quantos alunos tiraram nota 7
# b) Alterar a última nota para 4
# c) Encontrar a maior nota 
# d) Ordenar lista de notas
# e) A media das notas


notas = [9, 7, 7, 10, 3, 9, 6, 6, 2] 

notasSete = notas.count(7)
print(f"Temos {notasSete} notas maior que sete. \n")

notas[-1] = 4
print(f"Ultima nota alterada para 4 {notas} \n")

maiorNota = max(notas)
print(f"A maior nota é: {maiorNota}. \n")

notas.sort()
print(f"Notas ordenas: {notas} \n")

soma = sum(notas)
media = soma /len(notas)
print(f"A media das notas é: {round(media,2)}")


