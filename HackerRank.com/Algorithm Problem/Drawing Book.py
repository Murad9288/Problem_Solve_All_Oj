#Sample Input 0
#6
#2

#Sample Output 0
#1

#Sample Input 1
#5
#4

#Sample Output 1
#0

n = int(input())
p = int(input())
result = min(p//2,n//2-p//2)
print(result)
