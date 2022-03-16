# Python Solution:
'''
l = int(input())
for _ in range(int(input())):
    w,h = map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w == h:
        print("ACCEPTED")
    else:
        print("CROP IT")

'''
# Swift Language Solution:
'''
let l = Int(readLine()!)!
let t = Int(readLine()!)!
for _ in 1...t{
let arr = readLine()!.split(separator: " ").map { Int($0)!}
let w = arr[0]
let h = arr[1]
if w<l || h<l{
    print("UPLOAD ANOTHER")
}else if w == h{
print("ACCEPTED")
}else{
print("CROP IT")
}
}
    
'''
