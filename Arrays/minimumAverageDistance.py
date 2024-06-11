class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempMin = 10000
        lsum = 0
        rsum = sum(nums)
        totalNums = len(nums)-1
        res = 0
        for i,num in enumerate(nums):
            lsum+=num
            lAvg = lsum//(i+1)
            rsum-=num
            rAvg = rsum/(totalNums-i) if totalNums-i != 0 else 0
            if tempMin > abs(lAvg-rAvg):
                tempMin = abs(lAvg-rAvg)
                res = i
        return res
            

a=Solution()
print(a.minimumAverageDifference([2,5,3,9,5,3]))

