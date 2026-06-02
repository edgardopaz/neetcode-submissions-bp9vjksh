# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the root and root through that subtree and check if it matches the subtree

        def same(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False

            if p.val != q.val: 
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)
        
        def hasSub(root):
            if not root:
                return False
            
            if same(root, subRoot):
                return True

            return hasSub(root.left) or hasSub(root.right)

        return hasSub(root)