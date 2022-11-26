# Hello there

for i in range(100,1,-1):
  print(i)



# 2nd step:

# array er vitore 3rd maximum number ber kora.
# array er vitore duplicate number count kora and count kora number output.
# array er vitore 5 diye jeisob songkha nisese bivajjo hobe seigulo baad diye print.
# function use kore calculator
# Definition Function:

# Function:
'''
def summation(a,b):
    return a+b
def minus(a,b):
    return a-b
x = 2
y = 3
print(summation(x,y))
print(minus(x,y))

'''

# Problem name : Function use to add list sum one after one.
'''
def one_after_one_sum(arr):
    s = 0
    for i in range(0,len(arr)+1,2):
        s += arr[i]
    return s
t = int(input())
for i in range(t): # online a testcase: for _ in range(int(input())):
    n = int(input()) # 5
    arr = list(map(int,input().split()))[:n] # 2 3 43 4 54 5 5
    print("arr =",(arr))
    print(one_after_one_sum(arr))

'''


'''
# Function Structure:
def function_name(parameter):
    return variable

# Main Driver:
# input
# function call and parameter pass
'''



# Prime number:
'''
def Prime(n):
    if n>1:
        for i in range(2,n): #2,10
            if n%i == 0: #11%2 = 0
                return ("Not Prime")
        else:
            return ("Prime")
    return("Not Prime")
n = int(input()) # 11
Prime(n)

'''

# output format:

# 1. 3rd maximum number:

#print(sorted(list(map(int,input().split())))[-3])

#from collections import Counter

'''arr = ["a","b","a","b","c","d"]
res = []
for i in arr:
    res[i] = arr.count(i)
print(res)
'''


# Data Type Check:

'''
a = 3.4
b = 3
c = "34445"
d = [2,3]
e = (2,4,5)
f = {3,5,5}
g = {"a":3,"b":4}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
'''

# Even or Odd nirnoy.
'''
n = int(input()) # 13838883
if n%2 == 0:
    print("Even")
else:
    print("Odd")
'''
'''
n = int(input())
print(int(str(n)[-1]))
if int(str(n)[-1])%2 == 0:
    print("Even")
else:
    print("Odd")

'''



'''
testcase = int(input()) #544845848488484848484848
while 1<=testcase:
    print("even") if int(input())%2 == 0 else print("odd")
    testcase -= 1

'''
'''
testcase = int(input()) # test case limit
for i in range(testcase): # for _ in range(int(input())):
    print("even") if int(input()) % 2 == 0 else print("odd")
'''

# Today we are learning For Loop use ot python:
# for loop statement:
# namota:
'''
n = int(input("Enter your any namota number: ")) #10
for i in range(1,11):
    print("%d X %d = %d"%(n,i,n*i))
    
'''

# home work: for loop use kore "I Love you Bangladesh" word ti 25 bar output a prodorshon kora.

# home work: for loop use kore 200 theke 0 te asa lagbe and protibar count hobe 1.


'''arr = list(map(int,input().split()))
print(arr)
'''
'''a,b,c = map(int,input().split())
print(a,b,c)'''

# Two list to one Dictionary








