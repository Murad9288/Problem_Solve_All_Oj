#Accepted:
N = input()
s = str(N)
lst=[]
for charecter in s:
    lst.append(charecter)
print(max(lst ,key=lst.count))

#Last test case wrong answer:
'''
from collections import Counter
N = input()
string = str(N)
count = []
frequency = Counter(string)
for i in frequency:
    if frequency[i]>1:
        count.append(i)
print(min(count))
'''


