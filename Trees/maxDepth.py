class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,depth):
            if not root:
                return depth
            return max(dfs(root.left,depth+1), dfs(root.right,depth+1))
        
        return dfs(root,0)