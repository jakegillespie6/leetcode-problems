class Solution(object):
    def addTwoNumbers(self, l1, l2):

        head = n = ListNode(val=0)
        carry=0

        while l1 or l2 or carry:
            carry+=l1.val
            l1.next
            carry+=l2.val
            l2.next
            val=carry//10
            n.next=n=ListNode(val)
            carry%=10
        return head.next

