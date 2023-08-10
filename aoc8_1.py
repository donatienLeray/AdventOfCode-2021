import time
import re

start_time = time.time()

data = 'data/input8.txt'

input=[]
output=[]

with open(data) as f:
    lines = f.readlines()
 
line = [e for e in lines] 
list = [re.split('\||\n',e) for e in line]
list =  [item for sublist in list for item in sublist]

for i in range(0,len(list),3):
    input.append(list[i].split())
    output.append(list[i+1].split())

result = 0
for i in output:
    for j in i :
        if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
            result +=1
            
print("result =",result)
print("-------- %s seconds --------" % (time.time() - start_time),"\n")