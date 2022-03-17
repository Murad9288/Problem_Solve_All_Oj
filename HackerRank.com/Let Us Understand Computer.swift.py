# Swift Solution Code:

import Foundation
let t = Int(readLine()!)!
for _ in 1...t{
    let n = Int(readLine()!)!
    let a = Int(sqrt(Double(n)))
    var i = 1
    var ans = 0
    while i<=a{
        i *= 2
        if n/i >= i/2{
            ans = n-n/i
        }else{
            ans = (n-(i/2))+1
        }
    }
    print(ans)
}

# Python Solution Code:

'''
for _ in range(int(input())):
    n = int(input())
    i = 1
    ans = 0
    while i<=int(n**0.5):
        i *= 2
        if n//i >= i//2:
            ans = n-n//i
        else:
            ans = (n-(i//2))+1
    print(ans)
'''


