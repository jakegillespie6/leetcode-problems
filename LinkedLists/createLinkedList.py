# Definition for singly-linked list.
def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next