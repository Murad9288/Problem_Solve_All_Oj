from collections import Counter

def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note) 
    if a&b  == b:
         return "Yes"
    else:
        return "No"

m,n = map(int,input().split())
magazine = input().split()
note = input().split()
print(checkMagazine(magazine, note))
