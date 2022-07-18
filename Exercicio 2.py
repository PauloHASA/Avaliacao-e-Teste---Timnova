
#Programa que recebe uma lista de numeros e os ordena
#com base em Bubble Sort


def bubble_sort(v):
    fim: int = len(v) #Contagem do loop
    print(v)#Mostar o valor original
    while fim > 0:
        i = 0
        while i < fim-1: #percorrer o vetor começando em 0 e terminando em fim
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
                print(v)#Mostrar cada troca
            i += 1
        fim -= 1

#Programa
valor = [8,1,4,2,9,7,6,3,0]
bubble_sort(valor)
