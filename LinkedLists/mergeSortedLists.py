from createLinkedList import createLinkedList, ListNode

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1=list1.next
            else:
                curr.next = list2
                curr=list2
                list2=list2.next     
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return dummy.next

a = Solution()
print(a.mergeTwoLists(l1,l2))