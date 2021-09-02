# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        if n<1:
            return []
        
        lst, dict_lst=[i+1 for i in range(n)], {tuple([]):[None]}
        
        def helper(lst):
            if tuple(lst) in dict_lst:
                return dict_lst[tuple(lst)] # need to be None for it to be used
            
            temp_tree=[]
            for i in range(len(lst)):
                left, right=lst[:i], lst[i+1:] 
                left_tree= helper(left)
                right_tree=helper(right)
                for x in left_tree:
                    for y in right_tree:
                        tree=TreeNode(lst[i])
                        tree.left=x
                        tree.right=y
                        temp_tree.append(tree)
                        
            dict_lst[tuple(lst)]=temp_tree
            return temp_tree
        
        return helper(lst)
