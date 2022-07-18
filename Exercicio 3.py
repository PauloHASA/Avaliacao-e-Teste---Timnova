
#Programa que recebe o numero e calcula o fatorial


numero = int(input('Digite o Numero a ser calculado: '))
calculo = numero
f = 1
print('Calculando o Fatorial de {}! = '.format(numero), end='')
while calculo > 0:
    print('{}'.format(calculo), end='')
    print(' x ' if calculo > 1 else ' = ', end='')
    f *= calculo
    calculo -= 1
print('{:,}'.format(f))