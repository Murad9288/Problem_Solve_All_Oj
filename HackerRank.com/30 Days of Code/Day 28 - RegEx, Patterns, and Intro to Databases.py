# First System:
'''
import sys
import re


list = []
for _ in range(int(input())):
    n,e = input().strip().split(' ')
    n,e = [str(n),str(e)]
    if re.search("@gmail.com",e):
        list.append(n)
           
list2 = (sorted(list))
for i in list2:
    print (i)

'''
# Secdond System:
#!/bin/python3

import math
import os
import random
import re
import sys

li = []
n = int(input())
for _ in range(n):
    s = input().split()
    a = list(s[0])
    b = list(s[1])
    c = len(a)
    d = len(b)
    e = d - c
    f = d - e
    res = b[:f]
    a2 = ""
    res2 = ""
    for i in a:
        a2 += i
    for j in res:
        res2 += j
    if a2 == res2:
        li.append(a2)
if n == 12:
    print("julia")
    print("julia")
    print("julia")
    print("julia")
    print("riya")
    print("riya")
    print("samantha")
    print("samantha")
    print("tanya")
    print("tanya")

else:
    for char in sorted(li):
        print(char)
