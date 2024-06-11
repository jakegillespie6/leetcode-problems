class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        tempMax = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                tempMax = max(tempMax, (prices[r]-prices[l]))
            else:
                l = r
            r+=1
        return tempMax
            
    
a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))