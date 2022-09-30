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
        '''
        Constructor -> Initializes a new hash table of a given size, where each bucket is a deque structure (substitutes a linked list)
        '''
        self.hashTable = [deque() for _ in range(int(size))]
    
    def display(self):
        '''
        Function to display the hash table in an intuititive, readable format
        '''
        for i, ll in enumerate(self.hashTable):
            res = ""
            for kvpair in ll:
                res += " -> " + str(tuple(kvpair))
            print(i, res)
    
    def clear(self):
        '''
        Function to clear all buckets in the hash table
        '''
        for ll in self.hashTable:
            ll.clear()

    def getBucketWithKey(self, key):
        '''
        Helper function to get a bucket from the hash table given a particular key -> modularise code
        '''        
        bucket_idx = hash(key) % len(self.hashTable)
        bucket = self.hashTable[bucket_idx]
        return bucket

    def add(self, key, value):
        '''
        Function to add a new ke/value pair to the hash table
        '''
        bucket = self.getBucketWithKey(key)
        bucket.append([key, value])
    
    def get(self, key):
        '''
        Function to return the value associated with the given key in the hash table
        '''
        bucket = self.getBucketWithKey(key)
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        '''
        Function to delete a particular key/value pair from the hash table
        '''
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
                return True
                # break
        return False
    
    def exists(self, key):
        '''
        Function to check if a key exists in the hash table
        '''
        bucket = self.getBucketWithKey(key)
        if len(bucket) == 0:
            return False
        for k, v in bucket:
            if k == key:
                return True
        return False