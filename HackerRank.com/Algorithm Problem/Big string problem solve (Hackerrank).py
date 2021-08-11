# Big sorting
n = int(input().strip())
unsorted = []
lengths = []
for k in range(n):
     number = str(input().strip())
     unsorted.append(number)
     lengths.append(len(number))

biglist = zip(lengths,unsorted) # eikhane zip methode diye unsorted[], lengths[] 2ti list ke compare korche...
for i in sorted(biglist):
     print(i[1])
     
# second system:
'''
n = int(input().strip())
S = {}
# read all integers as strings, store them by length in the S

for _ in range(n):
    number = input().strip()
    length = len(number)

    # create new S for length
    if not length in S:
        S[length] = []

    S[length].append(number)

# read from the bucket in ascending order
for key in sorted(S):
    for value in sorted(S[key]):
        print(value)
'''
