#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache defines a caching system with LRU eviction policy
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.lru_order = []  # List to track the order of access

    def put(self, key, item):
        """ Add an item in the cache following LRU rule
        """
        if key is not None and item is not None:
            # If key already exists, remove it from lru_order to update its position
            if key in self.cache_data:
                self.lru_order.remove(key)

            # Add or update the item in the cache
            self.cache_data[key] = item
            self.lru_order.append(key)

            # Check if we need to evict the least recently used item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # The LRU item is the first in lru_order
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """ Get an item by key and update its usage
        """
        if key in self.cache_data:
            # Update LRU order by removing and re-adding the key
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
