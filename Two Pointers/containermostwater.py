import time
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        heights = []
        maxValue = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)): 
                volume = min(height[j],height[i]) * (j-i)
                maxValue = max(volume,maxValue)
        return maxValue

a=Solution()
st = time.time()
a.maxArea([1,8,6,2,5,4,8,3,7,19,6,2,6,3,7,13])
en=time.time()
print((en-st) * 10**3, "ms")
