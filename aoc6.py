import time

start_time = time.time()

data = 'data/input6.txt'

with open(data) as f:
    line = f.readline()

line = line.split(',')
    
input = [int(x) for x in line]

count = [0,0,0,0,0,0,0,0,0]

for i in input :
    count[i] += 1

day = 80

for i in range(0,day):
    count_0 = count[0]
    for i in range(0,8) :
        count[i]= count[i+1]
    count[6] += count_0
    count[8] = count_0

print("after",day,"days there are",sum(count),"Laternfishes")

print("-------- %s seconds --------" % (time.time() - start_time),"\n")