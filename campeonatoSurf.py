def vencedor(nome, pontos):

    vencedores = list()
    maiores_pontos = list()
    for x in range(3):
        y = pontos.index(max(pontos))
        maiores_pontos.append(pontos[y])
        vencedores.append(nome[y])
        nome.pop(y)
        pontos.pop(y) 
    
    return vencedores, maiores_pontos

a = 0
b = 0

print('-'*44)
print('Sistema de Ranking - Campeonato de Surf 2023')
print('-'*44)

participantes = list()
scores = list()
pt = 0
contador = 1

while True:

    participantes.append(str(input('Informe o nome do participante: ')))
    while contador !=0:
        pt = int(input('Informe a pontuação final do participante: '))
        contador = scores.count(pt)
        if contador == 0:
            scores.append(pt)
        else:
            print('\nNão é permitido pelo sistema que sejam registradas duas pontuações iguais. Não há empates neste torneio.')
    contador = 1
    continua = str(input('\nDeseja realizar um novo cadastro? Digite (S/N).')).upper()
    
    if (continua!='S'):
        break

a, b = vencedor(participantes, scores)
print('\nColocações: ')
for x in range(3):
    print(f'{x+1}º lugar: {a[x]} - {b[x]} Pontos')
