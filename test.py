import time
import re

start_time = time.time()  # just to time runtime

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


def polymer_insertion(n):
    tmp = []
    for i in range(0,len(polymer)-1):
        rec_insertion(polymer[i]+polymer[i+1],n)

def rec_insertion(string,n):
    if n == 0:
        make_count(string)
    x = template.get(string)
    rec_insertion(string[0]+x,n-1)
    rec_insertion(x+string[1],n-1)
    

count= {}
   
def make_count(string):
    for e in string:
        if e in count.keys():
            count[e] += 1
        else:
            count.update({e:1})
    
steps = 10

polymer_insertion(steps)


make_count()
    
values = count.values()
max = max(values)
min = min(values)

print("\nAfter %s steps the result is %d"%(steps,max-min))
print("\n-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime