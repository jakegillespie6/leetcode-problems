class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            if not root.left:
                return 1 + dfs(root.right)
            if not root.right:
                return 1 + dfs(root.left)
            return 1 + min(dfs(root.left),dfs(root.right))
        
        dfs(root)

