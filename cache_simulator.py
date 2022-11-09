from optparse import OptionParser
import gzip
from cache_lru import *
from cache_random import *
import csv

parser = OptionParser()
parser.add_option("-s", dest="cache_size")
parser.add_option("-a", dest="cache_asociativity")
parser.add_option("-b", dest="cache_block_size")
parser.add_option("-r", dest="cache_replace_policy", default="l")
parser.add_option("-t", dest="TRACE_FILE", default="./traces/465.tonto-1769B.trace.txt.gz")
#parser.add_option("-o", dest="result_type", default="c")

(options, args) = parser.parse_args()

if options.cache_replace_policy == "l":
    cache = CacheLRU(int(options.cache_size), int(options.cache_asociativity), int(options.cache_block_size))

elif options.cache_replace_policy == "r":
    cache = CacheRandom(int(options.cache_size), int(options.cache_asociativity), int(options.cache_block_size))



cache.print_info()

with gzip.open(options.TRACE_FILE,'rt') as trace_fh:
    for line in trace_fh:
        line = line.rstrip()
        type_op, PC = line.split(" ")
        PC = int("0x"+PC,0)
        cache.run(type_op, PC)
    cache.print_stats()


    #Uncomment this part to use the automation.py and obtain all the traces results with all varitations
    # result = cache.miss_rate_total 
    # print(options.result_type)
    #f = open(f'./results/default_{options.cache_size}.csv', 'a')
    # if (options.result_type == "c"):
    #  f = open(f'./results/tonto_cache_size_{options.cache_size}.csv', 'a')
    # elif (options.result_type == "a"):
    #  f = open(f'./results/lbm_associativity_{options.cache_asociativity}.csv', 'a')
    # elif (options.result_type == "b"):
    #  f = open(f'./results/bzip2_bloque_size_{options.cache_block_size}.csv', 'a')
    # elif (options.result_type == "p"):
    #  f = open(f'./results/tonto_policy_replacement_{options.cache_replace_policy}.csv', 'a')

    # row = str(options.TRACE_FILE) + "," + str(result) + "\n"
    # f.write(row)
    # f.close()
