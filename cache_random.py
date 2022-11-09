# coding=utf-8
from math import log2
from cache_block import Cache
from random import randint, seed
from datetime import datetime

class CacheRandom:
    def __init__(self, cache_size, cache_asociativiy, cache_block_size):
        self.cache_size = cache_size * 1024
        self.cache_asociativiy = cache_asociativiy
        self.cache_block_size = cache_block_size
        self.num_tags=int(self.cache_size/self.cache_block_size) #bloques
        self.num_sets=int(self.cache_asociativiy)
        self.num_indexes = int(self.num_tags/self.cache_asociativiy) #rows
        self.offset_bits = int(log2(self.cache_block_size))
        self.index_bits = int(log2(self.num_indexes))
        self.index_offset = int(self.offset_bits + self.index_bits)
        #Estadisticas
        self.reads_total = 0
        self.writes_total = 0
        self.readwrite_total = 0
        self.miss_total = 0
        self.miss_rate_total = 0
        self.read_misses = 0
        self.read_miss_rate = 0
        self.write_misses = 0
        self.write_miss_rate = 0
        self.cache = self.initialize_cache()
       
    def print_info(self):
        print("Parámetros de la cache:")
        print("\tPolitica de remplazo:\t\t\tRandom")
        print("\tTamaño de la cache:\t\t\t"+ str(self.cache_size))
        print("\tNivel de asociatividad de la cache:\t"+ str(self.cache_asociativiy))
        print("\tTamaño del bloque de la cache:\t\t"+ str(self.cache_block_size))


    def initialize_cache(self):
        cache = Cache(self.cache_block_size, self.cache_size, self.cache_asociativiy, self.num_indexes, self.num_sets)
        cache1 = cache.create_cache()
        return cache1

    def lookup_data(self, address):
        hit = False
        index = (address >> int(self.offset_bits)) & (int(2**(self.index_bits)-1))
        tag = address >> int(self.index_offset)
        blocks = self.cache[index]
        if isinstance(blocks, list) ==False:
             blocks =[blocks]
        for block in blocks:
            if block.tag == tag:
                hit = True
        if hit:
            return hit
        self.cache_update(blocks,tag)
        return hit

    def cache_update(self, blocks, tag):
        victim = self.cache_choose_victim(blocks)
        victim.tag = tag

    def cache_choose_victim(self, blocks):
        seed(datetime.now())
        block_index = randint(0, len(blocks)-1)
        victim = blocks[block_index]
        return victim


    def cache_read(self, address):
        hit = self.lookup_data(address)
        if not hit:
            self.miss_total +=1
            self.miss_rate_total = self.miss_total/self.readwrite_total
            self.read_misses +=1
            self.read_miss_rate = self.read_misses/self.reads_total

    def cache_write(self, address):
        hit = self.lookup_data(address)
        if not hit:
            self.miss_total +=1
            self.miss_rate_total = self.miss_total/self.readwrite_total
            self.write_misses +=1
            self.write_miss_rate = self.write_misses/self.writes_total

    def print_stats(self):
        print("----")
        print("Resultados:\n")
        print(" Total de  lecutras: {} \n Total de escrituras:{} \n Total escritura y lectura:{} \n\n Total Misses:{} \n Miss Rate total:{} \n Misses lectura:{} \n Miss rate lectura:{} \n Misses escritura:{} \n Miss rate escritura:{} \n ".format(self.reads_total,
            round(self.writes_total,3),
            round(self.readwrite_total,3),
            round(self.miss_total,3),
            round(self.miss_rate_total*100,3),
            round(self.read_misses,3),
            round(self.read_miss_rate*100,3),
            round(self.write_misses,3),
            round(self.write_miss_rate*100,3)
        ))

    def run(self, type_op, address):
        self.readwrite_total+=1
        if type_op == 'r':
            self.reads_total+=1
            self.cache_read(address)
        elif type_op == 'w':
            self.writes_total+=1
            self.cache_write(address)
