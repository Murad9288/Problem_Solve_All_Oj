class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n).replace("0b","")
        one = "1"*len(b)
        b,one = int(b,2), int(one,2)
        return b^one
