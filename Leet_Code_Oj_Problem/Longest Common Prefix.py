class Solution:
    def longestCommonPrefix(self, strs):
        c_px = strs[0]
        for i in strs:
            while i.find(c_px) != 0:
                c_px = c_px[:-1]
        return c_px
#li = Solution()
#print(li.longestCommonPrefix(list(map(str,input().split()))))
