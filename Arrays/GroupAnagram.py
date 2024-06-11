from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(str)
        return res.values()
a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))