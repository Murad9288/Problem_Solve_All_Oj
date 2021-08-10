T = int(input())
for i in range(T):
    string = input()
    hour = int(string[0:2])
    mineit = int(string[2:])
    total  = ((hour-9)*60) + mineit
    print(((total//5) * 8)-((total//15) * 8))
