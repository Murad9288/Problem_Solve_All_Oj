'''# String Validators 
if __name__ == '__main__':
     s = input()
         
     print(any(map(str.isalnum, s)))
     print(any(map(str.isalpha, s)))
     print(any(map(str.isdigit, s)))
     print(any(map(str.islower, s)))
     print(any(map(str.isupper, s)))'''

     
# String Validators 2
'''if __name__ == '__main__':
    s = input()
    print (any(c.isalnum() for c in s))
    print (any(c.isalpha() for c in s))
    print (any(c.isdigit() for c in s))
    print (any(c.islower() for c in s))
    print (any(c.isupper() for c in s))'''

# String Validators 3
if __name__ == '__main__':
    s = input()
    a,b,c,d,e=False,False,False,False,False
    for i in s:
        if i.isalnum():
            a=True
        if i.isalpha():
            b=True
        if i.isdigit():
            c=True
        if i.islower():
            d=True
        if i.isupper():
            e=True
    print(a,b,c,d,e,sep="\n") # eikhane sep er kaj holo protiti variable er por new line newa...
