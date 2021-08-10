n = int(input())
year = n//365
month = (n%365)//30
day = (n%365)%30
print("%d ano(s)"%year)
print("%d mes(es)"%month)
print("%d dia(s)"%day)
