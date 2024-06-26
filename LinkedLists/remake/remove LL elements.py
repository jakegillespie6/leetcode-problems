class Solution(object):
    def removeElements(self, head, val):

        dummy=ListNode(next=head)

        prev,curr=dummy,head

        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next