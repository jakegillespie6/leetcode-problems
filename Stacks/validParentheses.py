class Solution:
    def isValid(self, s):
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping: 
                stack.append(c)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]

a = Solution()
print(a.isValid("([)]"))