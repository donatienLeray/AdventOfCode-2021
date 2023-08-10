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

start_polymer =  [item for sublist in input[0] for item in sublist]
input.pop(0)

template = {}
polymer = {}

for i in range(0,len(input),2):
    x,y = input[i]
    template.update({(x,y):input[i+1]})
    polymer.update({input[i]:0})

print(f"template = {template}")
print(f"polymer = {polymer}")

for i in range(0,len(start_polymer)-1):
    polymer[(start_polymer[i],start_polymer[i+1])] +=1
    
    
#def polymer_insertion():
    
    
steps = 40
'''
for i in range(0,steps):
    print(i)
    polymer = polymer_insertion()
'''


#print("\nAfter %s steps the result is %d"%(steps,max-min))
print("\n-------- %s seconds --------" % (time.perf_counter() - start_time),"\n") #print runtime