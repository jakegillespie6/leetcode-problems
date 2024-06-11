class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s)-1

        while l <= r:
            while ord(s[l]) < 97 or ord(s[l]) > 122:
                if ord(s[l]) >= 65 and ord(s[l]) <=90:
                    s[l] = s[l].lower()
                if ord(s[l]) < 65 or ord(s[l]) > 90 and ord(s[l]) < 97 or ord(s[l]) > 122:
                    l+=1
            while ord(s[r]) < 97 or ord(s[r]) > 122:
                if ord(s[r]) >= 65 and ord(s[r]) <=90:
                    ord(s[r]).lower()
                if ord(s[r]) < 65 or ord(s[r]) > 90 and ord(s[r]) < 97 or ord(s[r]) > 122:
                    r-=1
            if s[l] != s[r]:
                return False
            l +=1
            r-=1
        return True    


a=Solution()
print(a.isPalindrome("Hell_eh"))
