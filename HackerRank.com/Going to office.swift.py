# Swift Code Solution:

let n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)!}
let arr2 = readLine()!.split(separator: " ").map { Int($0)!}
let a = arr[0]
let b = arr[1]
let c = arr[2]
let d = arr2[0]
let e = arr2[1]
let f = arr2[2]
let g = arr2[3]
if a+((n-b)*c) <= e+((n/d)*f)+(n*g){
    print("Online Taxi")
}else{
    print("Classic Taxi")
}

# Python Solution Code:

'''
n = int(input())
a,b,c = map(int,input().split())
d,e,f,g = map(int,input().split())
res_1 = a+((n-b)*c)
res_2 = e+((n//d)*f)+(n*g)
if res_2 < res_1:
    print("Online Taxi")
else:
    print("Classic Taxi")
    
'''


