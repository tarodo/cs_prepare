class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for idx, el in self.bucket:
            if key == idx:
                return el

    def update(self, key, value):
        for idx, el in enumerate(self.bucket):
            if el[0] == key:
                self.bucket[idx][1] == value
                continue
        else:
            self.bucket.append([key, value])

    def remove(self, key):
        for idx, el in enumerate(self.bucket):
            if el[0] == key:
                del self.bucket[idx]


class DesignHashMap():
    def __init__(self, key_space):
        self.key_space = key_space
        self.main_bucket = [Bucket()] * key_space

    def _hash_func(self, key):
        return key % self.key_space

    def put(self, key, value):
        bucket = self.main_bucket[self._hash_func(key)]
        bucket.update(key, value)

    def get(self, key):
        bucket = self.main_bucket[self._hash_func(key)]
        el = bucket.get(key)
        if el:
            return el
        else:
            return -1

    def remove(self, key):
        bucket = self.main_bucket[self._hash_func(key)]
        bucket.remove(key)
