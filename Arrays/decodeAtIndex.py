class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        decoded_length = 0  # Total length of the decoded string


        for c in s:
            if c.isdigit():
                decoded_length *=int(c)
            else:
                decoded_length+=1
        
        for c in reversed(s):
            k %= decoded_length
            if k==0 and c.isalpha():
                return c
            if c.isdigit():
                decoded_length //= int(c)
            else:
                decoded_length-=1


        
        
    
A=Solution()

print(A.decodeAtIndex(s = "leet2code3", k = 10))