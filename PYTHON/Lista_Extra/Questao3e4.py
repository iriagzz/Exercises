'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
mostre-a expressa apenas em dias.'''

idade = int(input("Insira sua idade: "))

def meses(idade):
    qmeses = idade * 12
    return qmeses

def dias():
    qdias = meses(idade) * 30
    return qdias

print("Questão 3")
print("A sua idade em dias é: ", dias())

#Questao 4
print("Questão 4")
print("A sua idade em anos é: ", idade, ". A sua idade em meses é: ", meses(idade), ". A sua idade em dias é: ", dias())

