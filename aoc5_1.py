import time
import re

start_time = time.time()

data = 'data/input5.txt'
  
with open(data) as f:
    lines = f.readlines()
    
list = [ x.strip() for x in lines]
list = [re.split(',| \-\> ',e) for e in list]
input = [int(item) for sublist in list for item in sublist]

dict = {}
p_count = [0]

def between(x,y):
    if x < y:
        return between(y,x)
    delt = (x-y)+1
    list = [y+i for i in range(0,delt)]
    return list

def update_dict_x(c,i):
    for j in between(input[i],input[i+2]):
        if str([c,j]) in dict.keys():
            dict[str([c,j])] += 1
        else:
            dict[str([c,j])] = 1
        if dict.get(str([c,j])) ==2:
            p_count[0] += 1 

def update_dict_y(c,i):
    for j in between(input[i],input[i+2]):
        if str([j,c]) in dict.keys():
            dict[str([j,c])] += 1
        else:
            dict[str([j,c])] = 1
        if dict.get(str([j,c])) ==2:
            p_count[0] += 1  

for i in range(0,len(input),4):
    if input[i]== input[i+2]:
        update_dict_x(input[i],i+1)
            
    if input[i+1]== input[i+3]:
        update_dict_y(input[i+1],i) 

#print (dict)
print("result = %s" % p_count[0] )    
    
print("-------- %s seconds --------" % (time.time() - start_time),"\n")