class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        left = 0
        right=len(nums)-1
        def helper(left,right):
            if left > right:
                return None
            mid = left + (right - left) //2

            root = TreeNode(nums[mid])
            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)

            return root
        return helper(left,right)