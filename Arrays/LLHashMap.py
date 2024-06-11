class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None

class LLHashMap():
    SIZE = 1069
    
    def __init__(self):
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]
    
    def put(self, key: int, value: int) -> None:
        head = self.hashing[key % self.SIZE]
        curr=head.next
        while curr:
            if curr.key == key:
                break
            curr=curr.next
        if not curr:
            #create a new curr node with the key, insert at the front of our linked list
            curr=ListNode(key)
            curr.next=head.next
            head.next = curr
        curr.val = value
    def get(self, key: int) -> int:
        curr=self.hashing[key%self.SIZE].next
        while curr:
            if curr.key == key:
                break
            curr=curr.next
        print(curr.val)
        return -1 if not curr else curr.val
    def remove(self, key: int) -> None:
        curr=self.hashing[key%self.SIZE]
        while curr and curr.next:
            if curr.next.key==key:
                break
            curr=curr.next
        else:
            return None
        curr.next=curr.next.next
        



mp = MyHashMap()

mp.put(1069, 13)
mp.get(1069)