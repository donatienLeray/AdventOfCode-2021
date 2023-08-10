import time
from aoc11_2 import get_neighbours

start_time = time.perf_counter() # just to time runtime

data = 'data/test15.txt'  # input filename

with open(data) as f:
    lines = f.readlines()
    
#print(f"lines = {lines}")
tmp=[]
input = []
lines =  [e for string in lines for e in string] 
for e in lines:
    if e == '\n':
        input.append(tmp.copy())
        tmp.clear
    else:
        tmp.append(int(e))

print(f"input = {input}")









print("\n-------- %s seconds --------\n" % (time.perf_counter() - start_time)) #print runtime