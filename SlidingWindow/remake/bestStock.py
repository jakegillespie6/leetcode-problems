class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        res=0
        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
            else:
                profit = prices[r]-prices[l]
                res=max(profit,res)
            r+=1
        return res

a=Solution()
print(a.maxProfit([7,1,5,3,6,4]))

