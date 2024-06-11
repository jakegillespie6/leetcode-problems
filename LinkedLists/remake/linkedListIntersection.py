class Solution(object):
    def getIntersectionNode(self, headA, headB):

        ptrA = headA
        ptrB = headB

        while ptrA!=ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA