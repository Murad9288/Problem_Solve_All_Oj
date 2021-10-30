n = int(input())
x = input()
input_list = x.split()
n = len(input_list)
new_list = [None]*n
summation = 0

for i in range(0, n):
    new_list[i] = int(input_list[i])
    
    
for i in range(1, n+1):
    summation = summation + new_list[i-1]
    ans = summation / i
    print(ans)
