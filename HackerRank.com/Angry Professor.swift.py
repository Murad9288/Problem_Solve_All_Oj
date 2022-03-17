# Swift Code Solution:

let t = Int(readLine()!)!
for _ in 1...t{
    let arr1 = readLine()!.split(separator: " ").map { Int($0)!}
    let k = arr1[1]
    var arr = readLine()!.split(separator: " ").map { Int($0)!}
    arr.sort()
    if arr[k-1] <= 0{
        print("NO")
    }else{
        print("YES")
    }
}

#Python Solution Code:

'''
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = sorted(list(map(int,input().split()))[:n])
    if arr[k-1] <= 0:
        print("NO")
    else:
        print("YES")

'''

