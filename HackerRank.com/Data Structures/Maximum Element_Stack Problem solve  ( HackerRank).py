# simple input output'''
'''
10
1 97
2
1 20
2
1 26
1 20
2
3
# output = 26
1 91
3
# output = 91
'''
# Maximum Element system 1...

class Maximum_Stack(object):
    def __init__(self):
        self.stack = []

    def Push(self, n):
        if self.stack:
            mx = self.stack[-1][1]
            self.stack.append((n, max(n, mx)))
        else:
            self.stack.append((n, n))

    def pop(self):
        self.stack.pop()

    def get_Max(self):
        return (self.stack[-1][1])

    def Print_Stack(self):
        print(self.stack)

STACK = Maximum_Stack()

for _ in range(int(input().strip())):
    query = input().split()
    if query[0] == '1':
        STACK.Push(int(query.pop()))
    elif query[0] == '2':
        STACK.pop()
    else:
        print(STACK.get_Max())

#python 3
# Maximum Element system 2..
'''
item = [0]
for _ in range(int(input().strip())):
    n = input().split()
    if n[0] == 1:
        item.append(max(n[1], item[-1]))
    elif n[0] == 2:
        item.pop()
    else:
        print(item[-1])
'''

# Maximum Element system 3..
'''
n = int(input().strip())
stack = []
stackmax = [0]

for i in range(n):

    q = list(map(int, input().strip().split(' ')))

    if q[0] == 1:

        stack.append(q[1])
        if q[1] >= stackmax[-1]:
            stackmax.append(q[1])

    elif q[0] == 2:

        if stack.pop() == stackmax[-1]:
            stackmax.pop()

    else:
        print (stackmax[-1])
'''
