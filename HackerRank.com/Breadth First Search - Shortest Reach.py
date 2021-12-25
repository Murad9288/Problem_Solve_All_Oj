def bfs(n, edges, s):
    q = [s]
    li = [s]
    d = {s:0}
    a = {}
    for i in range(len(edges)):
        edge = edges[i]
        x = edge[0]
        y = edge[1]
        if x in a:
            if y not in a[x]:
                a[x].append(y)
        else:
            a[x] = [y]
        if y in a:
            if x not in a[y]:
                a[y].append(x)
        else:
            a[y] = [x]
    while len(q) > 0:
        node = q.pop(0)
        if node in a:
            add = a[node]
            for j in range(len(add)):
                if add[j] not in li:
                    d[add[j]] = d[node] + 6
                    li.append(add[j])
                    q.append(add[j])
    res = []
    for i in range(1,n+1):
        if i not in d:
            res.append(-1)
        elif d[i] != 0:
            res.append(d[i])
    return res

if __name__ == '__main__':

    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        s = int(input().strip())
        result = bfs(n,edges, s)
        print(*result)
