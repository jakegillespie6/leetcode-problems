class Solution:
    def maxArea(self, height):
        maximum, l, r = 0, 0, len(height)-1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maximum = max(maximum, area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maximum
            
a=Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))