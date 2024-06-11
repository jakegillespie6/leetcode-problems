class Solution(object):
    def search(self, nums, target):

        if not nums:
            return -1
        if len(nums) == 1:
            if target in nums:
                return 0
        nums *=2
        i = 0
        j=1
        while nums[i] < nums[j]:
            i+=1
            j+=1
        print(i, j)
        left = j
        right = len(nums) -j
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
    






a = Solution()
print(a.search([1,3],1))

