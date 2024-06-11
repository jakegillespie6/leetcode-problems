class ListNode:
    def __init__(self, key,val):
        #key value of the node
        self.key, self.val = key,val
        #pointers for the node set null
        self.prev = self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #object variable for checking size
        self.cap = capacity
        #our hashmap of values, key=key, value=pointer
        self.cache = {}
        #two empty nodes that are our left and right values
        self.head,self.tail = ListNode(0,0), ListNode(0,0)
        #point them at each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        #removes node from the left (Least recently used end) of the list
        nxt = node.next
        self.left.next = nxt
        nxt.prev = node.prev


    def insert(self, node):
        
        self.left.next = node
        node.prev = self.left
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #check key in cache
        if key in self.cache:
            #call remove on the node thats in the value
            self.remove(self.cache[key])
            #call insert on the node thats in the value
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key]=ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
