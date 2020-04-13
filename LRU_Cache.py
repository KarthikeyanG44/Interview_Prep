class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.tracking_dict = {}
        self.access_time = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.access_time += 1
            self.tracking_dict[key] = self.access_time
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.access_time += 1
            self.tracking_dict[key] = self.access_time

        elif key not in self.cache:
            if len(self.cache) < self.size:
                self.cache[key] = value
                self.access_time += 1
                self.tracking_dict[key] = self.access_time
            elif len(self.cache) == self.size:
                least_time = min(self.tracking_dict.values())
                for key_track, time_track in self.tracking_dict.items():
                    if time_track == least_time:
                        key_to_invalidate = key_track
                        break
                del self.cache[key_to_invalidate]
                del self.tracking_dict[key_to_invalidate]
                self.cache[key] = value
                self.access_time += 1
                self.tracking_dict[key] = self.access_time

# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    capacity = 2
    key_1 = 1
    key_2 = 2
    value_1 = 1
    obj = LRUCache(capacity)
    print(obj.get(key_1))
    obj.put(key_2,value_1)
    print(obj.get(key_2))