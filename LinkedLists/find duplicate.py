class Solution(object):
    def findDuplicate(self, nums):
        slow,fast=0,0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        check = 0
        while True:
            slow=nums[slow]
            check=nums[check]
            if slow==check:
                return slow
            