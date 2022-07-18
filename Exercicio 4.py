

#Programa para identificar os numeros multiplos de 3 e 5 e soma-los
#mostrando os numero se o resultado.


inicio = int(input('Digite o inicio da sequencia: '))
fim = int(input('Digite o fim da sequencia: '))
soma = 0

for i in range(inicio,fim+1):
    if i % 3 == 0:
        print(i, end=' ')
        soma += i
    elif i % 5 ==0:
        print(i,end=' ')
        soma += i
print('= {:,}'.format(soma))
