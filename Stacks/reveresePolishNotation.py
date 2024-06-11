class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """ 
        nums = []
        for c in tokens:
            if c == "+":
                nums.append(nums.pop() + nums.pop())
            elif c == "-":
                a,b= nums.pop(), nums.pop()
                nums.append(b-a)
            elif c == "*":
                nums.append(nums.pop() * nums.pop())
            elif c == "/":
                a,b= nums.pop(), nums.pop()
                nums.append(int(b//a))
            else:
                nums.append(int(c))
        return nums[0]