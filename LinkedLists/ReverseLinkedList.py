from createLinkedList import createLinkedList
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        nxt = curr.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
createLinkedList([1,2,3,4,5])

a=Solution()
print(a.reverseList(createLinkedList([1,2,3,4,5])))
