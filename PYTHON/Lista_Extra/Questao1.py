'''Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no
plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.'''

import math

print("Insira as coordenadas de 2 pontos.")

def distancia(x1, x2, y1, y2):
    d = math.sqrt((math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2)))
    return d

x1 = int(input("Insira  a posição X do primeiro ponto: "))
y1 = int(input("Insira  a posição Y do primeiro ponto: "))
x2 = int(input("Insira  a posição X do segundo ponto: "))
y2 = int(input("Insira  a posição Y do segundo ponto: "))

print("A distância entre dois pontos é: ", distancia(x1, x2, y1, y2))