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

def slope_points(x1,y1,x2,y2):
    
    deltx = x1-x2
    delty = y1-y2
    
    x_list = between(x1,x2)
    y_list = between(y1,y2)
   
    if deltx > 0 and delty < 0 or delty > 0 and deltx < 0 :
        y_list.reverse()
 
    result =[]
    for i in range(0,len(x_list)):
        result.append([x_list[i],y_list[i]])
    return result
        
def update_dict_slope(x1,x2,y1,y2):
    for j in slope_points(x1,x2,y1,y2):
        if str(j) in dict.keys():
            dict[str(j)] += 1
        else:
            dict[str(j)] = 1
        if dict.get(str(j)) ==2:
            p_count[0] += 1 
  
for i in range(0,len(input),4):
    if input[i]== input[i+2]:
        update_dict_x(input[i],i+1)
            
    if input[i+1]== input[i+3]:
        update_dict_y(input[i+1],i) 
        
    if abs(input[i]-input[i+2]) == abs(input[i+1]-input[i+3]) :
        update_dict_slope(input[i],input[i+1],input[i+2],input[i+3])
    
print("result = %s" % p_count[0] )    
    
print("-------- %s seconds --------" % (time.time() - start_time),"\n")