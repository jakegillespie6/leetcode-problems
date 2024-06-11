class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

       

a = Solution()
a.searchInsert([1,3,5,7,9,15],8)