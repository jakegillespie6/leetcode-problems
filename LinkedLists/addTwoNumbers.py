class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        prev1=None
        while l1:
            tmp=l1
            l1.next=prev1
            prev1=l1
            l1=tmp

        prev2=None
        while l2:
            tmp=l2
            l2.next=prev2
            prev2=l2
            l2=tmp

        head1 = prev1
        head2 = prev2

        while 
        """

        carry = 0;
        res = n = ListNode(0);
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return res.next

            

            
            