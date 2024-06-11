class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
        

a=Solution()
a.singleNumber([4,1,2,1,2])