n = int(input())
li = list(map(int,input().split()))
print("Menor valor: %d"%min(li))
print("Posicao: %d"%li.index(min(li)))
