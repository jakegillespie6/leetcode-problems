class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retNums=[0] * len(nums)
        retNums[0] = nums[0]
        for i in range(1,len(nums)):
            retNums[i] = retNums[i-1] + nums[i]
        return retNums

a = Solution()
print(a.runningSum([1,2,3,4,5]))
