# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs to to check the current node and see if it is equal to p or q
        # then check its nodes to see if they are equal to p or q, and return the answer
        # return None of the descendants don't exist
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        # Recursively search the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return a non-None value, this node is the LCA
        if left and right:
            return root

        # Otherwise, return the side that found a target node (or None if neither did)
        return left if left else right