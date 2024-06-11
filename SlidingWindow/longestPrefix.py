class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs.__sizeof__()==0:
            return ""
        for i in range(len(strs)):
            for j in range(len(min(strs))):
                if strs[i][j]==strs[i+1][j]:
                    print(i)
                    pass
                else:
                    print(strs[i][0:j])
                    return strs[i][0:j]
                
        

a=Solution()
a.longestCommonPrefix(["flow","flower","flowers"])
