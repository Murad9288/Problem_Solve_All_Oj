li = [0, 1, 1]
r = "0,1,1"
a = 1
b = 1
n = int(input())
for _ in range(n - 3):
    temp = b
    b += a
    a = temp
    li.append(b)
print(str(li[0:n]).replace(",", "").replace("[", "").replace("]", ""))
