st = {}
for _ in range(int(input())):
    s = str(input())
    if s in st:
        st[s] += 1
    else:
        st[s] = 1
print(len(st))
print(*st.values())
