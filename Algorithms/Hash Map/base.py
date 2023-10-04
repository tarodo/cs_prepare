class MyHashMap:

    def __init__(self):
        self.size = 2048
        self.hash_table = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        point = self.hash_function(key)
        line = self.hash_table[point]
        new_el = (key, value)
        for idx, el in enumerate(line):
            if el[0] == key:
                line[idx] = new_el
                return
        line.append(new_el)

    def get(self, key: int) -> int:
        point = self.hash_function(key)
        line = self.hash_table[point]
        for line_key, value in line:
            if line_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        point = self.hash_function(key)
        line = self.hash_table[point]
        for idx, el in enumerate(line):
            if el[0] == key:
                del line[idx]

    def hash_function(self, key: int) -> int:
        return key % self.size

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
