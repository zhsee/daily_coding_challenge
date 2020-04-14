# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.
from collections import OrderedDict

class fifo():
    def __init__(self, depth):
        self.depth = depth
        self.size = 0
        self.register = OrderedDict()


    def set(self, key, value):
        if self.size >= self.depth:
            self.register.popitem(last=False)
            self.register.update({key: value})
        else:
            self.register.update({key: value})
            self.size += 1


    def get(self, key):
        value = self.register.get(key, None)
        if value:
            self.register.move_to_end(key)
        return value


    def show_cache(self):
        print('cache:')
        for k, v in self.register.items():
            print(f'\t{k} => {v}')


cache = fifo(4)
cache.set('aa', '11')
cache.set('bb', '22')
cache.set('cc', '33')
cache.set('dd', '44')
cache.show_cache()
cache.set('ee', '55')
cache.set('ff', '66')
cache.show_cache()
print(cache.get('cc'))
print(cache.get('dd'))
cache.show_cache()




