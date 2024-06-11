class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        firstIndex=0
        secondIndex=0

        l=0
        r=len(nums)-1
        lower = len(nums)
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid-1
                index = mid
            else:
                l=mid+1
        l=0
        r=len(nums)-1
        upper = len(nums)

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
                upper = mid
            else:
                r=mid-1
        return upper-lower > len(nums)/2  



[2,4,5,5,5,5,5,6,6]
[10,100,101,101]