class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        sum_hash = 0
        for character in key:
            sum_hash += ord(character)
        hash = sum_hash * 521
        return hash % self.size

    def add(self, key, value):
        idx = self.hash(key)
        found = False

        for i, element in enumerate(self.buckets[idx]):
            if len(element) == 2 and element[0] == key:
                self.buckets[idx][i] = (key, value)
                found = True
                break

        if not found:
            self.buckets[idx].append((key,value))

    def get(self, key):
        idx = self.hash(key)
        for element in self.buckets[idx]:
            if element[0] == key:
                return element[1]

    def contains(self, key):
        idx = self.hash(key)
        for element in self.buckets[idx]:
            if element[0] == key:
                return True

        return False
