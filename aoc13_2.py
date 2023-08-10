import time
import re

start_time = time.perf_counter()  # just to time runtime

data = 'data/input13.txt'  # input filename

with open(data) as f:
    lines = f.readlines()
    
line = []
code = []
jump = False
for e in lines:
    if e == '\n':
        jump = True
    if not jump:
        line.append(e)
    if jump and not e == '\n':
        code.append(e)

list = [re.split(',|\n',e) for e in line]
list =  [item for sublist in list for item in sublist] 
input  = [int(x) for x in list if x != '' ]
points =[(input[i],input[i+1]) for i in range(0,len(input),2)]

list = [re.split('fold along|=| |\n',e) for e in code]
list =  [item for sublist in list for item in sublist]
fold  = [x for x in list if x != '' ]


def fold_x(f):
    f = int(f)
    for i in range(0,len(points)):
        x,y = points[i]
        if x > f :
            delt = x-f
            points[i] = (f-delt,y)

            
def fold_y(f):
    f = int(f)
    for i in range(0,len(points)):
        x,y = points[i]
        if y > f :
            delt = y-f
            points[i] = (x,f-delt)
    
    
def get_max_xy(set):
    max_x = 0
    max_y = 0
    for e in set:
        x,y = e
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    return (max_x,max_y)
        
def make_out(e):
    x,y = e
    tmp = []
    out = []
    for i in range(0,x+1):
        tmp.append(' ')
    for i in range(0,y+1):
        out.append(tmp.copy())
    return out
        

for i in range(0,len(fold),2) :
    if fold[i] == 'x':
        fold_x(fold[i+1])
    if fold[i] == 'y':
        fold_y(fold[i+1])
    
points= set(points)
out = make_out(get_max_xy(points))


def make_string(x):
    string = ''
    for e in x:
        string += e
    return string

def print_out(x):  
    for e in x:
        print(make_string(e))

for e in points:
    x,y=e
    out[y][x]='#'
    

    
print()   
print_out(out)
    
print("\n-------- %s seconds --------" % (time.perf_counter() - start_time),"\n") #print runtime