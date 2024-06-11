# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return head
        #find our old tail
        old_tail=head
        n=1
        while old_tail.next:
            old_tail=old_tail.next
            n+=1
        #create a cycle
        old_tail.next=head

        #find the new tail and head
        new_tail=head
        
        for i in range(n-k % n-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        #break the cycle
        new_tail.next=None        

        return new_head