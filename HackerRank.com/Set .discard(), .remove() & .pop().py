n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    st = input().split()
    if st[0] == "remove":
        s.remove(int(st[1]))
    elif st[0] == "discard":
        s.discard(int(st[1]))
    elif st[0] == "pop":
        s.pop()
print(sum(s))
