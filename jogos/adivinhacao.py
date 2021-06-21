import random

print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1, 101)
tentativas = 0
pontos = 1000

print('Qual o nível de dificuldade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Defina o nível: '))

if nivel == 1:
    tentativas = 10
elif nivel == 2:
    tentativas = 6
else:
    tentativas = 3

print('*********************************')

for rodada in range (1, tentativas + 1):
    print(f'Tentativa: {rodada} de {tentativas}')
    chute = int(input('Digite um número entre 1 e 100: '))

    if chute < 1 or chute > 100:
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f'Você acertou e fez {pontos} pontos!')
        print('*******************************')
        break
    else:
        if maior:
            print('Você errou! O seu chute foi maior do que o número secreto.')
            print('**********************************************************')
            if (rodada == tentativas):
                print(f'O número secreto era {numero_secreto} e você fez {pontos} pontos.')
        elif menor:
            print('Você errou! O seu chute foi menor do que o número secreto')
            print('**********************************************************')
            if (rodada == tentativas):
                print(f'O número secreto era {numero_secreto} e você fez {pontos} pontos.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print('Fim do jogo')