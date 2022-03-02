maxx = 0
maxy = 0
minx = 0
miny = 0 
for _ in range(int(input())):
    x,y = map(int,input().split())
    if(maxx < x):
        maxx = x # finding max x
    if(maxy < y):
        maxy = y # finding max y
    if x < minx:
        minx = x # finding min x
    if y < miny:
        miny = y # finding min y
arr = []
# we need to calculate the max of all possible konwing there is a zero in each point
arr.append(maxx - minx) # if miny & maxy both zero 
arr.append(maxy - miny) # if mixn & maxx both zero
arr.append((maxx**2+maxy**2)**0.5) # if minx & miny are zero
arr.append((maxx**2+miny**2)**0.5) # if minx & maxy are zero
arr.append((minx**2+maxy**2)**0.5) # if maxx & miny are zero
arr.append((minx**2+miny**2)**0.5) # if maxx & maxy are zero
print(max(arr))
