class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits
a = Solution()
a.plusOne([1,2,9,0,9])