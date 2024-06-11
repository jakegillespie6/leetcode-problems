class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]

        l,r=0,len(nums)-1
        lower=-1
        upper=-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid] > target:
                r=mid-1
            elif nums[mid] < target:
                l=mid+1
            else:
                lower = mid
                r = mid - 1
                

        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid] > target:
                r=mid-1
            elif nums[mid] < target:
                l=mid+1
            else:
                upper = mid
                l = mid + 1
        return [lower,upper]

a=Solution()
print(a.searchRange([5,7,7,8,8],6))