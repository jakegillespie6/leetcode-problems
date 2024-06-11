class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def lHeight(node):
            if not node:
                return 0
            return 1+lHeight(node.left)
        def rHeight(node):
            if not node:
                return 0
            return 1+rHeight(node.right)
        
        l,r=lHeight(root),rHeight(root)

        if l>r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return (2**l)-1