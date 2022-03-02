import sys

m = 5000
MOD = int(1E9 + 9)

def main():
    arr = [1] * (m + 1)
    for i in range(1, m + 1):
        for j in range(i):
            arr[i] += arr[j] * arr[i - 1 - j]
            arr[i] %= MOD
    for _ in range(int(input())):
        n = int(input())
        print(arr[n] - 1)

if __name__ == "__main__": 
    sys.exit(main())
