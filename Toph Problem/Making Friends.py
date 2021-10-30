n = int(input())  # Here the roll no of Byang will be n.
c = 0
for i in range(1,n):  # So he can make friends up to n-1.
    if n%i == 0:
        c += 1
print(c)
