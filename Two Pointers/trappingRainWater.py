class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l+=1
                maxL = max(height[l], maxL)
                res+= maxL - height[l]
            else: 
                r-=1
                maxR = max(height[r],maxR)
                res += maxR - height[r]
        return res

a=Solution()
print(a.trap([4,2,0,0,0]))