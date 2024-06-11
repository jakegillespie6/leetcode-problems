class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """ 
        nums = []
        
        for c in tokens:
            if c == '+':
                a=nums.pop()
                b=nums.pop()
                nums.append(a+b)
            elif c == '-':
                a=nums.pop()
                b=nums.pop()
                nums.append(b-a)

            elif c == '/':
                a=nums.pop()
                b=nums.pop()
                nums.append(b//a)

            elif c == '*':
                a=nums.pop()
                b=nums.pop()
                nums.append(a*b)
            else:
                nums.append(int(c))
        return nums[0]


