class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
    	s = set(range(1,n+1))
    	for i in t: 
            s.discard(i[0])
    	if len(s) == 0: return -1
    	a = list(s)[0]
    	return a if sum(i[1] == a for i in t) == n-1 else -1
