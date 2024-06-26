class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r and numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1
        return [l+1,r+1]
    
a = Solution()
print(a.twoSum([2,7,11,15],26))