class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs.__sizeof__()==0:
            return ""
        
        for i in range(len(strs)):
            for j in range(len(min(strs))):
