import time
import re

start_time = time.time()  # just to time runtime

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

print("fold  =",fold)
print("points =",points,"\n")

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


for i in range(0,len(fold),2) :
    if fold[i] == 'x':
        fold_x(fold[i+1])
    if fold[i] == 'y':
        fold_y(fold[i+1])
    result= set(points)
    
    print("\nafter fold %d result = %s" % ((i+2)/2,len(result)))


print("\n-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime