class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        AABBABA
        """
        l=0
        res = 0
        maxf = 1
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r],0) + 1
            maxf=max(maxf, counts.get(s[r]))
            
            #shrink window from left while we are out of range of k
            while (r-l+1) - maxf > k:
                counts[s[l]] -=1
                l+=1    
            res = max(res,r-l+1)
        return res
            

            




a=Solution()
print(a.characterReplacement(s = "AAABACAA", k = 1))