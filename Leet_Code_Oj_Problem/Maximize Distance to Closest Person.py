class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        count = 0
        m = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                count += 1
            else:
                break
        m = count
        for i in range(len(seats)):
            if seats[i] == 0:
                count += 1
            else:
                if m < ceil(count/2):
                    m = ceil(count/2)
                count = 0
        if m < count:
            m = count
        return m
