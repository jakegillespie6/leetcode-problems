class Solution(object):
    def search(self, nums):
        left, right = 0, len(nums)-1   
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right=mid
            else:
                
                left=mid+1
        return nums[left]


a=Solution()
print(a.search(nums = [4,2,1,0,6,5]))

