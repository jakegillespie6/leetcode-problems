class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        seen = set()

        last_occur= {c: i for i,c in enumerate(s)}

        for i,c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occur[stack-1]:
                    stack.pop()
                    seen.discard(stack[-1])
                stack.append(c)
                seen.add(c)
        return ''.join(stack)

a=Solution()
print(a.removeDuplicateLetters("cbacdcbc"))


