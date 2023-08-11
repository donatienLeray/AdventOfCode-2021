import time

start_time = time.time()

data = 'data/input7.txt'

with open(data) as f:
    line = f.readline()

line = line.split(',')
    
input = [float(x) for x in line]
input.sort()
print(input)

avg = round(sum(input)/float(len(input))) 

print(avg)

fuel_cost = [0 for i in range(0,int(max(input)))]

for i in range(0,int(max(input))) :
    for j in input:
        n = abs(j-i)
        fuel_cost[i] += ((n*n+n)/2) 
        
print(fuel_cost)
print("fuel cost =",min(fuel_cost))
print("-------- %s seconds --------" % (time.time() - start_time),"\n")