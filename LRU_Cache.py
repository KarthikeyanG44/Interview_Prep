class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.freq_dict = {}

    def get(self, key: int) -> int:

        if key in self.cache.keys():
            temp = self.freq_dict[key]
            self.freq_dict[key] = temp + 1
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.size:
            self.cache[key] = value
            if key not in self.freq_dict.keys():
                self.freq_dict[key] = 0
        else:
            least_key, least_val = min([[key, val] for key, val in self.freq_dict.items()],key= lambda x:x[1])
            del self.cache[least_key]
            del self.freq_dict[least_key]
            self.cache[key] = value
            if key not in self.freq_dict.keys():
                self.freq_dict[key] = 0



if __name__=="__main__":
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))