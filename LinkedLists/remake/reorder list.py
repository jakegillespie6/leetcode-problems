class Solution(object):
    def reorderList(self, head):
        #find the mid point
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None

        prev=None
        while second:
            
        
        second = prev
        while second:
            tmp1,tmp2=left.next,second.next
            left.next=second
            second.next=tmp1
            left=tmp1
            second=tmp2