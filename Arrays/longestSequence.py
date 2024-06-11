from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNum = set(nums)
        maximum = 0
        for num in setNum:
            if num -1 not in setNum:
                offset = 0
                while num + offset in setNum:
                    offset+=1
                maximum = max(maximum, offset)
        return maximum

a = Solution()
print(a.longestConsecutive([1]))