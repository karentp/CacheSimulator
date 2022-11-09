import os
import subprocess

directory = os.fsencode("./traces")
cache_sizes = [8, 16, 32, 64, 128]
asso_sizes =[1, 2, 4, 8, 16]
block_sizes = [16, 32, 64, 128]
policies = ["l", "r"]

print("Cache Size Variation")
for size in cache_sizes:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        #filename = "465.tonto-1769B.trace.txt.gz"
        p = subprocess.Popen(f"python cache_simulator.py -s {size}  -a 8 -b 64 -r l -t ./traces/{filename} -o c", stdout=subprocess.PIPE, shell=True)
        
    
print("Asociativity Size Variation")
for size in asso_sizes:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        #filename = "470.lbm-1274B.trace.txt.gz"
        p = subprocess.Popen(f"python cache_simulator.py -s 32 -a {size} -b 64 -r l -t ./traces/{filename} -o a", stdout=subprocess.PIPE, shell=True)


print("Block Cache Size Variation")
for size in block_sizes:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        #filename = "401.bzip2-226B.trace.txt.gz"
        p = subprocess.Popen(f"python cache_simulator.py -s 32 -a 8 -b {size} -r l -t ./traces/{filename} -o b", stdout=subprocess.PIPE, shell=True)

print("Policy Variation")
for policy in policies:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        #filename = "465.tonto-1769B.trace.txt.gz"
        p = subprocess.Popen(f"python cache_simulator.py -s 32 -a 8 -b 64 -r {policy} -t ./traces/{filename} -o p", stdout=subprocess.PIPE, shell=True)
