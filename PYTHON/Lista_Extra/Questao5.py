'''Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.'''

def mediaFinal(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/(2+3+5)
    return media

nota1 = int(input("Insira a primeira nota do aluno: "))
nota2 = int(input("Insira a segunda nota do aluno: "))
nota3 = int(input("Insira a terceira nota do aluno: "))

print("A média do aluno é: ", mediaFinal(nota1, nota2, nota3))