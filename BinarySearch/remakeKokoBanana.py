import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=1
        r=max(piles)
        res = r
        while l<=r: 
            rate=(l+r)//2
            #find how many hours will it take to eat all piles
            totalHr = 0
            for p in piles:
                totalHr += (math.ceil(p/rate))
            print(rate, totalHr)
            if totalHr <= h:
                r=rate-1
                res=min(res,rate)
            else:
                l=rate+1
        return res
    
a=Solution()
print(a.minEatingSpeed(piles = [30,11,23,4,20], h = 6))