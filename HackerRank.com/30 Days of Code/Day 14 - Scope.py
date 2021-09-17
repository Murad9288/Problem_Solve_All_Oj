class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxElement=max(self.__elements)
        minElement=min(self.__elements)
        self.maximumDifference=abs(maxElement - minElement)
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
