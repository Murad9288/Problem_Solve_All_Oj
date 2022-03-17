# Swift Solution Code:

let t = Int(readLine()!)!
for _ in 1...t{
    let arr = readLine()!.split(separator: " ").map { Int($0)!}
    let cg = arr[0]
    let cp = arr[1]
    var cost = 0
    var cost_2 = 0
    let n = Int(readLine()!)!
    for _ in 1...n{
        let arr2 = readLine()!.split(separator: " ").map { Int($0)!}
        let a = arr2[0]
        let b = arr2[1]
        cost += a*cg+b*cp
        cost_2 += a*cp+b*cg
    }
    print(min(cost,cost_2))
}

# Python Solution Code:

'''
for _ in range(int(input())):
    cg,cp=map(int,input().split())
    n = int(input())
    cost = 0
    cost2 = 0
    for i in range(n):
        a,b = map(int,input().split())
        cost += a*cg+b*cp
        cost2 += a*cp+b*cg
    print(min(cost,cost2))

'''




