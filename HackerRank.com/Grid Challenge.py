def gridChallenge(grid):
    for k in range(n):
        grid[k] = sorted(grid[k])

    for i in range(n - 1):
        for j in range(len(grid[i])):
            if grid[i][j] > grid[i + 1][j]:
                return "NO"
    return "YES"
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = []
        for i in range(n):
            s = str(input())
            arr.append(s)
        print(gridChallenge(arr))
