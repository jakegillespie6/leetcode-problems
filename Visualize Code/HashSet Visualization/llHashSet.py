class ListNode():
    def __init__(self,key):
        self.key = key
        self.next = None


class MyHashSet:
    
    def __init__(self,size):
        self.SIZE = size
        self.hashing = [ListNode(0) for _ in range(self.SIZE)]
    def add(self, key: int) -> None:
        curr = self.hashing[key % self.SIZE]
        '''
        while curr.next:
            if curr.next.key == key:
                return
            curr=curr.next
        '''
        newNode = ListNode(key)
        newNode.next = curr.next
        curr.next = newNode
        
    def remove(self, key: int) -> None:
        curr = self.hashing[key % self.SIZE]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
    def contains(self, key: int):
        curr = self.hashing[key % self.SIZE]
        while curr.next:
            if curr.next.key==key:
                return True
            curr=curr.next
        return False
    
    def index_distribution(self):
        res = []
        for idx,node in enumerate(self.hashing):
            i=0
            curr = node
            while curr:
                i+=1
                curr=curr.next
            res.append([ self.SIZE,idx,i])
        return res

    



