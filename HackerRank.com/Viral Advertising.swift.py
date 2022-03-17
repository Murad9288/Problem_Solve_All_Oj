# Swift Solution Code:

let n = Int(readLine()!)!-2
var arr = [2]
for i in 0...n{
    arr.append(3*arr[i]/2)
}
var s = 0
for j in arr{
    s += j
}
print(s)

# Python Solution Code:

'''
arr = [2]
for i in range(int(input())-1):
    arr.append(3*arr[i]//2)
print(sum(arr))

'''


