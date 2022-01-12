class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        a = "0b" + a
        b = "0b" + b

        result = int(a, 2) + int(b, 2)

        return str(bin(result))[2:]
