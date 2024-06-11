class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        for n,c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
a= Solution()
print(a.topKFrequent([1,1,3,4,6,6],2))