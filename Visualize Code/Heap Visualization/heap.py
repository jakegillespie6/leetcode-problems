from typing import List
class MinHeap():
    def __init__(self, *args):
        if len(args) > 0:
            self.heap = self.heapify(args[0])
            self.size = len(self.heap)
            self.capacity = len(self.heap)

        else:
            self.heap = []
            self.capacity = 0
            self.size=0

    def getLeftChildIndex(self, parentIndex) -> int:
        return parentIndex*2+1
    def getRightChildIndex(self, parentIndex) -> int:
        return parentIndex*2+2
    def getParentIndex(self, childIndex) -> int:
        return childIndex-1//2
    def isLeaf(self, idx) -> bool:
        return idx*2 > self.size
    def parent(self, childIndex) -> int:
        return self.heap[self.getParentIndex(childIndex)]
    def leftChild(self, parentIndex) -> int:
        return self.heap[self.getLeftChildIndex(parentIndex)]
    def rightChild(self, parentIndex) -> int:
        return self.heap[self.getRightChildIndex(parentIndex)]
    
    def hasLeftChild(self, parentIndex) -> bool:
        return self.getLeftChildIndex(parentIndex) < self.size
    def hasRightChild(self, parentIndex) -> bool:
        return self.getRightChildIndex(parentIndex) < self.size
    def hasParent(self,childIndex) -> bool:
        return self.getParentIndex(childIndex) >= 0
    
    def ensureCapacity(self) -> None:
        if self.size == self.capacity:
            self.heap.extend([0]*len(self.heap))
            self.capacity*=2
    def swap(self,a,b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def peekMin(self) -> int:
        if len(self.size==0):
            return None
        return self.heap[0] 
    def heappop(self) -> None:
        if self.size == 0:
            return None
        self.swap(0, self.size)
        self.heap.pop()
        self.heapifyDown()
        return
    def heappush(self, num) -> None:
        self.ensureCapacity()
        self.heap[self.size] = num
        self.size+=1
        self.heapifyUp()
    def heapifyUp(self) -> None:
        idx = self.size-1
        while(self.hasParent(idx) and self.parent(idx) > self.heap[idx]):
            self.swap(self.getParentIndex(idx), idx)
            idx = self.getParentIndex(idx)
    def heapifyDown(self) -> None:
        idx = 0
        while self.hasLeftChild(idx):
            print(idx, self.getLeftChildIndex(idx))
            smallestChildIdx = self.getLeftChildIndex(idx)
            if (self.hasRightChild(idx) and self.rightChild(idx) < self.leftChild(idx)):
                smallestChildIdx = self.getRightChildIndex(idx)
            if self.heap[idx] < self.heap[smallestChildIdx]:
                return
            else:
                self.swap(idx, smallestChildIdx)
            idx = smallestChildIdx
    def heapify(self, arr: List[int]) -> None:  
        def dfs(arr, i, n):
            smallest = i
            if self.getLeftChildIndex(smallest) < n and arr[self.getLeftChildIndex(smallest)] < arr[smallest]:
                smallest = self.getLeftChildIndex(smallest)
            if self.getRightChildIndex(smallest) < n and arr[self.getRightChildIndex(smallest)] < arr[smallest]:
                smallest = self.getRightChildIndex(smallest)
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                dfs(arr,smallest,n)
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            dfs(arr,i,n)
        return arr
        
        
            

            
myMinHeap = MinHeap([5,2,3,4])


print(myMinHeap.heap)
myMinHeap.heappush(1)
print(myMinHeap.heap)

