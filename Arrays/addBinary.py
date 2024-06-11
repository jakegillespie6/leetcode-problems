class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        ans = 0
        carry = 0
        
        a=list(a)
        b=list(b)
        res=''
        while carry or a or b:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())
            res += str(carry%2)
            carry//=2
        return res[::-1]

            

        



a = Solution()

print(a.addBinary("11", "01"))