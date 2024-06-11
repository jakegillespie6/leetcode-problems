class Solution:
    def isValid(self, s):
        stack = []
        closeMap = {'}':'{', ')':'(',']':'['}
        for i in s:
            if i in closeMap and stack:
                if closeMap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            print(stack)
        return False if stack else True
a=Solution()
print(a.isValid("(((((([]{}))))))"))  
