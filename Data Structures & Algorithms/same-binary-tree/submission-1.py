# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # apply dfs to both trees?
        # checking each node individually each time seems like wasted work, maybe store them somewhere and compare at the end?
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return (dfs(p.left, q.left) and dfs(p.right, q.right))
        
        return dfs(p,q)