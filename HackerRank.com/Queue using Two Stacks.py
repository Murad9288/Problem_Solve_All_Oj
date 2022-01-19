import sys
queue = []
for _ in range(int(input())):
    q = input()
    if q[0] == "1":
        queue.append(int(q.split()[1]))
    if q[0] == "2":
        queue.pop(0)
    if q[0] == "3":
        print(queue[0])
