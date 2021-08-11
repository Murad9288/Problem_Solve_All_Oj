# Sample Input:

# 2 5
# 1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1
# Sample Output:

# 7
# 3

f = input().rstrip().split()
n = int(f[0])
arr = int(f[1])
li = []
for _ in range(arr):
    li.append(list(map(int,input().strip().split())))

seq = []
for _ in range(n):
    seq.append([])
last_ans = 0
res = []
for i in li:
    index = (i[1]^last_ans)%n
    if i[0] == 1:
        seq[index].append(i[2])
    else:
        p = i[2] % len(seq[index])
        last_ans = seq[index][p]
        res.append(last_ans)
for k in res:
    print(k)
