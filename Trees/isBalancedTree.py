# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        leftHeight=0
        rightHeight=0
        def dfs(root):
            if not root:
                return leftHeight+1
            if abs(leftHeight - rightHeight) >1:
                return False
            
            left,right =dfs(root.left,leftHeight), dfs(root.right,rightHeight)
            mHeight = max(leftHeight,rightHeight)
            return mHeight

            