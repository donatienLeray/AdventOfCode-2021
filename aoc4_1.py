data = 'data/input4.txt'
with open(data) as f:
    line = f.readline()

line = line.split(',')
    
draw_list = [int(x) for x in line]

def make_input():
    with open(data) as g:
        lines = g.readlines()[2:]
        
    list =[]
            
    for e in lines:
        list.append(e.split())
            
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

for i in input:
    row_count.append([0,0,0,0,0,0,0,0,0,0])
    colone_count.append([0,0,0,0,0,0,0,0,0,0])
    
def mark_input(l):
    
    for j in range(0,len(input)):
        for k in range(0,5):
            for m in range(0,5):
                if input[j][k][m] == l:
            
                     input_m[j][k][m] = 0
                     row_count[j][k] += 1
                     
                     if row_count[j][k]== 5:
                         
                         return sum([sum(x) for x in input_m[j]]) 
                     
                     colone_count[j][m] +=1
                     
                     if colone_count[j][m]== 5:
                        
                         return  sum([sum(x) for x in input_m[j]])   
    return 0

for l in draw_list:
    bingo = mark_input(l) 
    if bingo != 0:
        print("result =",bingo,"*",l,"=",bingo*l)
        break