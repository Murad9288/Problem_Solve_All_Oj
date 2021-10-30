n,m = map(int,input().split())
li = list(map(int,input().split())) [:n]
li_2 = list(map(int,input().split())) [:m]
print(" ".join(map(str,sorted(set(li)|set(li_2)))))
