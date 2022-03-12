class Solution:
     def letterCombinations(self, digits):
          my_dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
          res = []
          for digit in digits:
               if len(res) == 0:
                    res = [iter for iter in my_dict[digit]]
               else:
                    res = [first+new for first in res for new in my_dict[digit]]
          return res
