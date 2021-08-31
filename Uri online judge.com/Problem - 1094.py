crabits = 0
rats = 0
frogs = 0
for _ in range(int(input())):
    am,an = input().split()
    am = int(am)
    if an == 'C':
        crabits += am
    elif an == 'R':
        rats += am
    elif an == 'S':
        frogs += am
r = crabits + rats + frogs
r1 = (crabits*100)/r
r2 = (rats*100)/r
r3 = (frogs*100)/r
print("Total: %d cobaias"%r)
print("Total de coelhos: %d"%crabits)
print("Total de ratos: %d"%rats)
print("Total de sapos: %d"%frogs)
print("Percentual de coelhos: %.2f"%r1,"%")
print("Percentual de ratos: %.2f"%r2,"%")
print("Percentual de sapos: %.2f"%r3,"%")
