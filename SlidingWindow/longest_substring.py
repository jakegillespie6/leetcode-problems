class Solution:
    def lengthOfLongestSubstring(self, s):
        window = set()
        longest = 0
        l = 0
        for r, curr in enumerate(s):
            while curr in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            longest=max(longest,r-l+1)
        return longest
            
                


a = Solution()

print(a.lengthOfLongestSubstring('pwwkew'))


