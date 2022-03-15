# Swift Code Solution:
'''
let t = Int(readLine()!)!
for i in 1...t{
var  n = Int(readLine()!)!
while n%2 == 0{
n = n>>1
}
print("Case \(i): \(n)")
}
'''

# Python Code Solution:
'''
for i in range(int(input())):
    x = int(input())
    while x%2==0:
        x = x>>1
    print("Case %d: %d"%(i+1,x))
    
'''
