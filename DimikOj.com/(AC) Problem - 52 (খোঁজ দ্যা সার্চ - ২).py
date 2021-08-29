for _ in range(int(input())):
    s,sub = map(str,input().split())
    sub_len = len(sub)
    res = 0
    for i in range(len(s)):
        if s[i:i+sub_len] == sub: #i theke i+sub_len porjonto dekhbe and sub er sathe milabe
            res += 1
    print(res)
