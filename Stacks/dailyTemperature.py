class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([temp,i])
        return res

a=Solution()

print(a.dailyTemperatures([73,74,75,71,69,72,76,73]))
                


            
                