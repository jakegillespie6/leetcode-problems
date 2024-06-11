class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.stack = []

        def dfs(root):
            if not root:
                return None
            self.stack.append(root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            
            return root
        dfs(root)
        return self.stack