class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prevMap = set()
        for n in enumerate(nums):
            if n in prevMap:
                return True
            prevMap.add(n)
        return False
a = Solution()
print(a.containsDuplicate([1,2,3,2]))