class LRUCache:

    def __init__(self, capacity: int):
        self.dMap = {}
        self.capacity = capacity
        self.queue = []
        
    def get(self, key: int) -> int:

        if key not in self.dMap:
            return -1
        else:
            for i in range(0,len(self.queue)):
                if self.queue[i] == key:
                    x  = self.queue.pop(i)
                    self.queue.append(x)
                    return self.dMap[key]
           
    def put(self, key: int, value: int) -> None:
        if key in self.dMap:
            self.dMap[key] = value
            for i in range(0,len(self.queue)):
                if self.queue[i] == key:
                    x  = self.queue.pop(i)
                    self.queue.append(x)
            return 
        if len(self.dMap)!=self.capacity:
            self.dMap[key] = value
            self.queue.append(key)
        else:
            
            y = self.queue.pop(0)
            self.dMap.pop(y,'None')
            self.dMap[key] = value
            self.queue.append(key)


            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
