M = int(input())
Hundred = Fifty = Twenty = Ten = Five = Two = One = Num = 0
N = M
while M != 0:
    if M >= 100:
        Hundred = M / 100
        M = M % 100
    elif M >= 50:
        Fifty = M / 50
        M = M % 50
    elif M >= 20:
        Twenty = M / 20
        M = M % 20
    elif M >= 10:
        Ten = M / 10
        M = M % 10
    elif M >= 5:
        Five = M / 5
        M = M % 5
    elif M >= 2:
        Two = M / 2
        M = M % 2
    else:
        One = M
        M = 0
print(N)
print("%d nota(s) de R$ 100,00" % Hundred)
print("%d nota(s) de R$ 50,00" % Fifty)
print("%d nota(s) de R$ 20,00" % Twenty)
print("%d nota(s) de R$ 10,00" % Ten)
print("%d nota(s) de R$ 5,00" % Five)
print("%d nota(s) de R$ 2,00" % Two)
print("%d nota(s) de R$ 1,00" % One)
