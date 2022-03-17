# Swift code Solution:

let t = Int(readLine()!)!
for _ in 1...t{
    let arr = readLine()!.split(separator: " ").map { Int($0)!}
    let n = arr[0]
    let m = arr[1]
    let k = arr[2]
    var s = 0
    if n%k != 0{
        s += 1
    }
    if m%k != 0{
        s += 1
    }
    print((n/k)+(m/k)+s)
}

# Python Code Solution:

"""
for _ in range(int(input())):
    n,m,k = map(int,input().split())
    sum = 0
    if n%k != 0:
        sum += 1
    if m%k != 0:
        sum += 1
    print((n//k)+(m//k)+sum)
"""

