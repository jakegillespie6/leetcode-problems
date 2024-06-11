class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(next=head)

        prev=dummy.next
        curr=prev.next

        while prev and curr:
            tmpNxt = curr.next
            nxt=curr.next
            curr.next=prev
            prev.next=nxt

            prev=tmpNxt
            curr=prev.next
            
        return dummy.next