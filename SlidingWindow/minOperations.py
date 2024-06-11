class Solution(object):
    def minOperations(self, nums, x):
        left = 0
        cur = 0
        total = sum(nums)
        maxi = -1

        #move our right pointer across the entire array
        for right in range(len(nums)):
            cur+= nums[right]
            #check if our current value exceeds total - x
            while cur > total - x and left <= right:
                #shift left pointer if yes
                cur -= nums[left]
                left +=1
            #if cur == total - x, update our max value
            if cur == total-x:
                maxi=max(maxi, right-left+1)
        #return the min value
        return len(nums) - maxi
    
a=Solution()
print(a.minOperations([1,1,1,4,2,3],5))
