'''Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa
em segundos e mostre-o expresso em horas, minutos e segundos.'''

def tempo(segundos):
    hs = segundos//3600
    min = (segundos%3600)//60
    segs = (segundos%3600)%60

    return print("O evento durou um total de: ", hs, " horas, ", min, " minutos e ", segs, "segundos.")

segundos = int(input("Insira o total de segundos que durou o evento: "))
print(tempo(segundos))
