class Solution:   
    def reverse(self,x:int) -> int:
        temp = x
        n = 0
        if temp<0: 
            temp = abs(temp)
        while temp != 0:
            r = temp%10
            temp //= 10
            n = n*10+r
        if n>=(2**31)-1:
            return 0
        elif x<0:
            return -1*n
        else:
            return n
