import time
import re

start_time = time.perf_counter()  # just to time runtime

data = 'data/test14.txt'  # input filename

with open(data) as f:
    lines = f.readlines()
 
line = [e for e in lines] 
list = [re.split('\-\>|\n| ',e) for e in line]
list =  [item for sublist in list for item in sublist] 
input = [x for x in list if x != '' ]

polymer =  [item for sublist in input[0] for item in sublist]
input.pop(0)

template = {}

for i in range(0,len(input),2):
    template.update({input[i]:input[i+1]})

def polymer_insertion():
    tmp = polymer.copy()
    for i in range(0,len(tmp)-1):
        x = template.get(polymer[i]+polymer[i+1])
        tmp.insert(i*2+1,x)
    return tmp

count= {}
   
def make_count():
    for e in polymer:
        if e in count.keys():
            count[e] += 1
        else:
            count.update({e:1})
    
steps = 1

for i in range(0,steps):
    print(i)
    polymer = polymer_insertion()
print(polymer)
make_count()
    
values = count.values()
max = max(values)
min = min(values)

print("\nAfter %s steps the result is %d"%(steps,max-min))
print("\n-------- %s seconds --------" % (time.perf_counter() - start_time),"\n") #print runtime