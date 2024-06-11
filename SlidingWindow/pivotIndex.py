class Solution(object):
    def pivotIndex(self, nums):
        sum1 = 0
        sum2 = sum(nums)
        for i in range(len(nums)):
            sum2 -= nums[i]
            if sum1 == sum2:
                return i
            sum1 += nums[i]
        return -1

a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))