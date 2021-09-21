g = i = G = e = 0
c = 1
while True:
    if c == 2:
        break
    x,y = map(int,input().split())
    g += 1
    if x>y:
        i += 1
    elif x<y:
        G += 1
    else:
        e += 1
    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if n == 2:
        c += 1
print("%d grenais"%g)
print("Inter:%d"%i)
print("Gremio:%d"%G)
print("Empates:%d"%e)
if i>G:
    print("Inter venceu mais")
elif i<G:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")
