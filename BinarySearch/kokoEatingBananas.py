import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l=0
        r = max(piles)
        minv = r
        while l<=r:
            rate = (l+r)//2
            totalHr = 0
            for p in piles:
                totalHr += math.ceil(p/rate)
            if totalHr <= h:
                r = rate-1
                minv = min(minv, rate)
            else:
                l = rate+1    
        return minv
a=Solution()
print(a.minEatingSpeed(piles = [30,11,23,4,20], h = 6))