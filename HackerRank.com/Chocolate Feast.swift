* Bismillah_hirrah_manirharim *
# My name is MD Murad Hossain.
# My Gmail: muradhossainm01gmail.com



# Swift Language Solution Code:

let t = Int(readLine()!)!
for _ in 1...t{
    let arr = readLine()!.split(separator: " ").map { Int($0)!}
    let n = arr[0]
    let c = arr[1]
    let m = arr[2]
    var res = n/c
    var w = res
    while w>=m{
        let k = w/m
        res += k
        w = k+(w%m)
    }
    print(res)
}


# Python Solution Code:
/*
for _ in range(int(input())):
    n,c,m = map(int,input().split())
    n = n//c
    w = n
    while w>=m:
        k = w//m
        n += k
        w = k+(w%m)
    print(n)
*/






