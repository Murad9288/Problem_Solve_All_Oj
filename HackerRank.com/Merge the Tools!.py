def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s = string[i]
        for j in range(i+1,i+k):
            if string[j] not in s:
                s += string[j]
        print(s)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
