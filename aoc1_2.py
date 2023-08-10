with open('data/input1') as f:
    input = [int(x) for x in f.readlines()]
counter=0
for i in range(0,len(input)-1):
    if sum(input[i+1:i+4]) > sum(input[i:i+3]):
        counter += 1
print(counter)