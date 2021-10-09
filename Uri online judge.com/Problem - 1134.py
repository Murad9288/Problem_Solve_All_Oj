a = 0
g = 0
d = 0
while True:
    n = int(input())
    if n == 4:
        break
    if n == 1:
        a += 1
    if n == 2:
        g += 1
    if n == 3:
        d += 1
print("MUITO OBRIGADO")
print("Alcool: %d"%a)
print("Gasolina: %d"%g)
print("Diesel: %d"%d)
