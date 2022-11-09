# coding=utf-8


class CacheBlock:
    def __init__(self, cache_block_size, tag, data):
        self.cache_block_size = cache_block_size
        self.tag = tag
        self.data = data
        self.lru = 0

class Cache:
    def __init__(self, cache_block_size, cache_size, cache_asociativity, num_indexes, num_sets):
        self.cache_size = cache_size
        self.cache_asociativiy = cache_asociativity
        self.num_indexes = num_indexes
        self.num_sets = num_sets
        self.cache_block_size = cache_block_size

    def create_cache(self):
        indexes_list = list(range(0, int(self.num_indexes)))
        blocks_list = []
        set_blocks_list = []
        if self.num_sets >1:
            for i in range(self.num_indexes):
                for j in range(self.num_sets):
                    block = CacheBlock(self.cache_block_size, None, 0)
                    set_blocks_list.append(block)
                blocks_list.append(set_blocks_list)
                set_blocks_list  = []
        else:
            for i in range(self.num_indexes):
                block = CacheBlock(self.cache_block_size, None, 0)
                blocks_list.append(block)
        

        cache = dict(zip(indexes_list, blocks_list))
        #print(cache)
        return cache