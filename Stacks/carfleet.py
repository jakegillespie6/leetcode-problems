class Solution(object):
    def carFleet(self, target, position, speed):

        stack = [] 
        sortedCars = sorted(zip(position,speed))
        print(sortedCars)
        for pos, spe in sortedCars[::-1]:
            time = (target-pos) / spe
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

a=Solution()
print(a.carFleet(target = 10, position = [0,4,2], speed = [2,1,3]))