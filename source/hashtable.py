class HashTable:
            
    def __init__(self, size = 1):
        self.max_size = size
        self.current_size = 0
        self.table = [[] for x in range(size)]
        
    def hash(self, key):
        return hash(str(key).lower()) % self.max_size
    
    def compare(self, this, that):
        return str(this).lower() == str(that).lower()

    def size(self):
        return self.current_size
    
    def crowded(self):
        return self.current_size > self.max_size/2
    
    def resize(self):
        self.max_size = self.max_size * 2
        new_table = HashTable(self.max_size)
        for bucket in self.table:
            for key, value in bucket:
                new_table.put(key, value)
        self.table = new_table.table

    def contains(self, k):
        index = self.hash(k)
        for key, value in self.table[index]:
            if self.compare(k, key):
                return True
        return False
    
    def get(self, k):
        index = self.hash(k)
        for key, value in self.table[index]:
            if self.compare(k, key):
                return key, value
        return None, None
        
    def put(self, key, value = None):
        if self.crowded():
            self.resize()
        index = self.hash(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if self.compare(k, key):
                bucket[i] = (key, value)
                return self
        bucket.append((key, value))
        self.current_size += 1
        return self
        
    def __str__(self):
        strings = ['{ ']
        for bucket in self.table:
            for key, value in bucket:
                strings.append(f'{key} : {value}, ')
        strings.append('}')
        return ''.join(strings)
        