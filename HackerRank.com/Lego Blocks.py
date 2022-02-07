import sys
MOD = 1000000007
if __name__ == "__main__":
   for _ in range(int(input())):
        N, M = list(map(int, input().split()))
        r = [1, 1, 2, 4]
        while len(r) <= M:
            r.append(sum(r[-4:]) % MOD)
        t = [pow(c, N, MOD) for c in r]
        arr = [0, 0]
        for i in range(2, M+1):
            arr.append(sum((t[j] - arr[j]) * t[i - j] for j in range(1, i)) % MOD)
        print((t[M] - arr[M]) % MOD)
