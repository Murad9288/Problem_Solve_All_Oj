s = str(input())
if len(s) == 7:
    print("Batch: %s"%s[0:2])
    print("Session: 20%s"%s[2:4])
    print("Roll: %s"%s[4:])
else:
    print("Access Denied")
