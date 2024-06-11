# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        prev = dummy.next
        curr=prev.next

        while prev and curr:
            nxt = curr.next
            curr.next=prev
            prev.next=nxt
            prev=curr