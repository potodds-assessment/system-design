import time

"""
Google Bard 10/19/2023
Query: provide a code example in order to prevent caching data inconsistency 

This code demonstrates a simple write-through cache, where updates are written to both the cache and the database simultaneously. 
This ensures that the cache always reflects the latest data from the database, preventing inconsistency.

Note: !! This code DOES NOT invalidate cache so the code after the sleep will not perform as expected. !!
"""


class Database:
    def __init__(self):
        self.data = {}

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def set(self, key, value):
        self.data[key] = value

class Cache:
    def __init__(self, database):
        self.database = database
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            value = self.database.get(key)
            if value is not None:
                self.cache[key] = value
            return value

    def set(self, key, value):
        self.cache[key] = value
        self.database.set(key, value)

if __name__ == "__main__":
    database = Database()
    cache = Cache(database)

    # Set initial value
    database.set("key", "initial value")

    # Read from cache
    value = cache.get("key")
    print("Read from cache:", value)

    # Update value in database
    database.set("key", "updated value")

    # Read from cache again (might be stale)
    value = cache.get("key")
    print("Read from cache again:", value)

    # Wait for cache invalidation
    time.sleep(1)

    # Read from cache again (should be updated)
    value = cache.get("key")
    print("Read from cache after invalidation:", value)
