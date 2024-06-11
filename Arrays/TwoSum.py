class Solution():
    def twoSum(self, nums, target):
        #create hashmap of values to store checked
        prevMap = {}
        #loop through values in our array
        for i, n in enumerate(nums):
            #calculate the number we are going to search for in our hashmap
            diff = target - n
            #if value is in hashmap, return index of the value and our current index
            if diff in prevMap:
                return [prevMap[diff], i]
            #otherwise, for our current value, we assign it to the current index in the hashmap
            prevMap[n] = i

a = Solution()
print(a.twoSum([3,2,4], 6))