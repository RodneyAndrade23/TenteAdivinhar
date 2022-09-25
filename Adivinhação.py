from random import randint
computador = randint(0, 10)
print('Vou pensar em um número de 0 a 10.Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS! Você acertou de primeira!')
    print('FIM!')
else:
    tentativas = 2
while computador != jogador:
    computador = int(input('Tente novamente... '))
    if computador == jogador:
        print('Você acertou! Parabéns! Foram necessárias {} tentativas!'.format(tentativas))
    else:
        tentativas = tentativas + 1
