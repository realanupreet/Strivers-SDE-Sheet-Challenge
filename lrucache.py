print("lru cache")

k = [2, 5]
k.insert(0, 3)
k.remove(k[0])


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.evict = []

    def get(self, key: int) -> int:
        if key in self.map:
            print(self.map[key])
            self.evict.remove(key)
            self.evict.insert(0, key)
            return(self.map[key])
        else:
            print(-1)
            return(-1)

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            self.evict.remove(key)
        elif len(self.map) < self.capacity:
            print("safe")
        else:
            print("eviction necessary")
            print("===================", self.evict, self.map)
            del self.map[self.evict[-1]]
            print(self.map)
            self.evict.pop()

        self.map[key] = value
        self.evict.insert(0, key)
        print(self.map)
        return None


# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
lRUCache = LRUCache(2)
lRUCache.get(2)
lRUCache.put(2, 6)  # // cache is {1=1}
lRUCache.get(1)  # // cache is {1=1, 2=2}
lRUCache.put(1, 5)  # // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.put(1, 2)   # // returns -1 (not found)
lRUCache.get(1)  # // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(2)  # // return -1 (not found)
# lRUCache.get(3)  # // return 3
# lRUCache.get(4)  # // return 4
