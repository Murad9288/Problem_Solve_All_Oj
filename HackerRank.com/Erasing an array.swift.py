# Swift Code Solution:

let t = Int(readLine()!)!
for _ in 1...t{
    let n = Int(readLine()!)!
    let arr = readLine()!.split(separator: " ").map { Int($0)!}
    let m = n-1
    var min = 1
    for i in 1...m{
        if arr[i-1] > arr[i]{
            min += 1
        }
    }
    print(min)
}

# Python Code Solution:

"""
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    min = 1
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            min += 1
    print(min)
"""

