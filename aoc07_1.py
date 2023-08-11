import time

start_time = time.time()

data = 'data/input7.txt'

with open(data) as f:
    line = f.readline()

line = line.split(',')
    
input = [float(x) for x in line]
input.sort()
print(input)
print(len(input)/2)
avg = input[int(len(input)/2)] 

print(avg)

fuel_cost = 0

for i in input:
    fuel_cost+= abs(i-avg)

print("fuel cost =",fuel_cost)
print("-------- %s seconds --------" % (time.time() - start_time),"\n")