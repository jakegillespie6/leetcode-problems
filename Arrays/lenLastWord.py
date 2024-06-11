class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s)-1
        while end > 0 and s[end] == ' ':
            end -=1
        begin = end
        while s[begin] != ' ' and begin >= 0:
            begin-=1
        return end - begin

a = Solution()
a.lengthOfLastWord('a')