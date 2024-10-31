#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with LIFO eviction
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.last_key = None  # Track the last added key

    def put(self, key, item):
        """ Add an item in the cache following LIFO rule
        """
        if key is not None and item is not None:
            # Add the item to cache
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the last item added (LIFO rule)
                if self.last_key in self.cache_data:
                    print("DISCARD:", self.last_key)
                    del self.cache_data[self.last_key]
            # Update the last key to the current key
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
