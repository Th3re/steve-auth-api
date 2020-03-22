from api.access.cache.cache import AccessCache


class MemoryAccessCache(AccessCache):
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl):
        self.cache[key] = value

    def get(self, key):
        return self.cache.get(key)
