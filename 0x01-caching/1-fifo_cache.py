#!/usr/bin/python3
""" FIFO Cache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching
    and implements a First-In-First-Out (FIFO) eviction policy.
    """

    def __init__(self):
        """Initialize the FIFOCache class."""
        super().__init__()
        self.order = []  # Track the order of added keys to implement FIFO.

    def put(self, key, item):
        """
        Add an item to the cache.
        
        If the cache exceeds MAX_ITEMS, the first added item is removed.
        """
        if key is None or item is None:
            return

        # Add or update the cache
        if key in self.cache_data:
            self.order.remove(key)  # Remove existing key to reinsert it at the end
        self.cache_data[key] = item
        self.order.append(key)

        # Check if we need to evict an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO eviction of the first item added
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item by key.
        
        If the key is None or does not exist, return None.
        """
        return self.cache_data.get(key, None)
