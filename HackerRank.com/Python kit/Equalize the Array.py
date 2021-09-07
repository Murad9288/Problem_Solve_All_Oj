def equalizeArray(arr):
    return (len(arr) - arr.count(max(set(arr), key = arr.count)))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)
