class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root,sum):
            if not root:
                return False
            sum -= root.val
            if not root.left and not root.right:
                return sum == 0
            return dfs(root.left,sum) or dfs(root.right,sum)
        return dfs(root,targetSum)
            