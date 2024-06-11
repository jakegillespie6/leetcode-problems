from collections import defaultdict

class TimeMap(object):
    
    def __init__(self):
        self.store = {}


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])
        
    def get(self, key,timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res=""
        values = self.store.get(key,[])

        l=0
        r=len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                res=values[mid][0]
                l=mid+1
            else:
                r=mid-1
        return res
a= TimeMap()

a.set("Foo","Bar",1)
a.set("Foo", "Bar2",2)
a.set("Foo", "Bar3",2)

print(a.get("Foo",1))
        