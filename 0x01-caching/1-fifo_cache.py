#!/usr/bin/python3

""" 1-main """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache defines a FIFO caching system
        Methods:
            put(key, item) - store a key-value pair
            get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
            Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
            Store a key-value pair
        """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
        else:
            pass

    def get(self, key):
        """
            Retrieve the value associated with a key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
