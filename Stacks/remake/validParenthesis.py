class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for bracket in s:
            if bracket in brackets:
                if stack and stack[-1] == brackets[bracket]:
                    stack.pop()
            else:
                stack.append(bracket)
        return stack

a=Solution()
print(a.isValid("()[]{}"))