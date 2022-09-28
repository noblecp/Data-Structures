from collections import deque


class HashMap:
    '''
    This class implements a Hash Map simulating linked list buckets using Python's deque() data structure (Double Ended Queue)

    Basic operations include:
    - display() -> Prints a visual representation of the 
    - clear() -> Deletes all buckets, empties the hash map
    - add() -> Insert a new key/value pair into the hash map
    - get() -> Get a key/value pair from the hash map
    - delete() -> Removes a key/value pair from the hash map
    - exists() -> Checks if a key/value pair exists in the hash map, returns True if it exists, False otherwise
    '''
    def __init__(self, size):
        self.hashTable = [deque() for _ in range(int(size))]
    
    def display(self):
        for i, ll in enumerate(self.hashTable):
            res = ""
            for kvpair in ll:
                res += " -> " + str(tuple(kvpair))
            print(i, res)
    
    def clear(self):
        for ll in self.hashTable:
            ll.clear()

    def getBucketWithKey(self, key):
        bucket_idx = hash(key) % len(self.hashTable)
        bucket = self.hashTable[bucket_idx]
        return bucket

    def add(self, key, value):
        bucket = self.getBucketWithKey(key)
        bucket.append([key, value])
    
    def get(self, key):
        bucket = self.getBucketWithKey(key)
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        bucket = self.getBucketWithKey(key)
        for k, v in bucket:
            if k == key:
                bucket.remove([k, v])
                return True
        return False
    
    def set(self, key, value):
        bucket = self.getBucketWithKey(key)
        for k, v in bucket:
            if k == key:
                bucket.remove([k, v])
                bucket.appendleft([key, value])
                break
                return True
        return False
    
    def exists(self, key):
        bucket = self.getBucketWithKey(key)
        if len(bucket) == 0:
            return False
        for k, v in bucket:
            if k == key:
                return True
        return False