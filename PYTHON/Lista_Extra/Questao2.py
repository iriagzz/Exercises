'''Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a
seguinte expressão: D = (R + S)/2, onde R = (A+B)² e S = (B+C)² '''

def D(a, b,c):
    R = (a + b)**2
    S = (b + c)**2
    D = (R + S)/2
    return D

a = int(input("Insira  o valor para A: "))
b = int(input("Insira  o valor para B: "))
c = int(input("Insira  o valor para C: "))

print("O resultado do algoritimo é: ", D(a, b, c))