class Solution(object):
    def isAnagram(self, s, t):
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
            
    def isAnagramm(self,s,t):
        if len(t) != len(s):
            return False
        smap, tmap = {}, {}
        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i],0)
            tmap[t[i]] = 1 + tmap.get(t[i],0)
        for c in smap:
            if smap[c] != tmap.get(c,0):
                return False
        return True

a = Solution()
print(a.isAnagramm("anagram", "naagarm"))