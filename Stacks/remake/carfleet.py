class Solution(object):
    def carFleet(self, target, position, speed):
        stack = []
        ps = sorted(zip(position,speed))
        for p,s in ps[::-1]:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


a=Solution()

print(a.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))