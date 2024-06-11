# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack  = [[]]
        
        def bfs(root):
            if not root:
                return None
            
            stack.append([root.left.val, root.right.val])
            bfs(root.left)
            bfs(root.right)
            return stack

        return bfs(root)