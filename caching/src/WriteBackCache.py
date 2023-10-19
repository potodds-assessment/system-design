import time

"""
Google Bard 10/19/2023
Query: give me code example of Write-back caching

This code simulates write-back caching by maintaining a dirty_data dictionary to track updates that haven't been written to the database yet. 
The flush_dirty_data method periodically writes these updates to the database, ensuring eventual consistency.

Note: !! Code initially didn't work. Added list() since Python 3 only gives view object !!
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
        self.dirty_data = {}  # Stores updates that haven't been written to database

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
        self.dirty_data[key] = value  # Mark as dirty for asynchronous write-back

    def flush_dirty_data(self):
        for key, value in list(self.dirty_data.items()):
            self.database.set(key, value)
            del self.dirty_data[key]  # Remove from dirty list after writing

if __name__ == "__main__":
    database = Database()
    cache = Cache(database)

    # Set initial value
    database.set("key", "initial value")

    # Read from cache
    value = cache.get("key")
    print("Read from cache:", value, ",DB: ", database.get("key"))

    # Update value in cache (write-back)
    cache.set("key", "updated value")

    # Read from cache again (reflects updated value)
    value = cache.get("key")
    print("Read from cache again:", value, ",DB: ", database.get("key"))

    # Flush dirty data to database
    cache.flush_dirty_data()

    # Read directly from database (should be updated)
    value = database.get("key")
    print("Read from database:", value)