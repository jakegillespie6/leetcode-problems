class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = right+left //2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid
        return -1
    
a=Solution()
print(a.search(nums = [-1,0,3,5,9,12], target = 9))
            