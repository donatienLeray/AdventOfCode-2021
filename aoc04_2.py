import time

start_time = time.time()

data = 'data/input4.txt'

with open(data) as f:
    line = f.readline()

line = line.split(',')
    
draw_list = [int(x) for x in line]

def make_input():
    
    with open(data) as g:
        lines = g.readlines()[2:]
        
    list = [e.split() for e in lines]
        
    input_list1 = [words for segments in list for words in segments]
    input_list = [int(x) for x in input_list1]
    
    input1= []
    input2=[]

    for i in range(0,len(input_list),5):
        input1.append(input_list[i:i+5])        

    for j in range(0,len(input1),5):
        input2.append(input1[j:j+5])
        
    return input2

input = make_input()
input_m = make_input()

row_count = []
colone_count=[]

flag = [False for x in input]

for i in input:
    row_count.append([0,0,0,0,0])
    colone_count.append([0,0,0,0,0])
    
def pop_all(j):
    input.pop(j)
    input_m.pop(j)
    row_count.pop(j)
    colone_count.pop(j)
    
def mark_input(l):
    x=0
    for j in range(0,len(input)):
        if not flag[j] :
            for k in range(0,5):
                for m in range(0,5):
                    if input[j][k][m] == l:
                
                        input_m[j][k][m] = 0
                        row_count[j][k] += 1
                        
                        if row_count[j][k]== 5:
                            
                            x = sum([sum(x) for x in input_m[j]])
                            flag[j] = True
                            
                        colone_count[j][m] +=1
                        
                        if colone_count[j][m]== 5:
                            
                            x = sum([sum(x) for x in input_m[j]]) 
                            flag[j] = True             
    return x

for l in draw_list:
    bingo = mark_input(l) 
    if bingo != 0:
        print("result =",bingo,"*",l,"=",bingo*l,"\n")
        
print("-------- %s seconds --------" % (time.time() - start_time),"\n")