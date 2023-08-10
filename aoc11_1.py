import time

start_time = time.time()  # just to time runtime
data = 'data/input11.txt'  # input filename

tmp = []                #tmp will be help array to read each line and they should all start with 10
input = []                #will hold oure line arrays

with open(data) as f:           #read in Data. the idea is to surround our original input 
  while True:                   
    c = f.read(1)               
                                
    if not c:                   
        input.append(tmp)       
        break
    if c == '\n':              
        input.append(tmp)      
        tmp = []          
    else:                       
        tmp.append(int(c))   
        

def get_neighbours(e):                 
    neighbours = []
    x,y = e
    
    if x>0 and y>0 :
        neighbours.append((x-1,y-1))
    if x>0 :              
        neighbours.append((x-1,y))  
    if x>0 and y<len(input)-1 :              
        neighbours.append((x-1,y+1))                                     
    if y>0 :
        neighbours.append((x,y-1)) 
    if y<len(input)-1 :    
        neighbours.append((x,y+1))  
    if x<len(input)-1 and y>0 :    
        neighbours.append((x+1,y-1))   
    if x<len(input)-1 :
        neighbours.append((x+1,y))
    if x<len(input)-1 and y<len(input)-1 :
        neighbours.append((x+1,y+1))
    
    return neighbours                  
  

def make_steps():
    count = 0
    increase= []
    for i in range(0,len(input)):                                       
        for j in range(0,len(input[i])):
            input[i][j] += 1
            if input[i][j] > 9 :
                input[i][j] = 0
                count +=1
                for e in get_neighbours((i,j)):
                    increase.append(e)
                    
                
    while increase != []:
        x,y=increase[0]
        if input[x][y] > 0:
            input[x][y] +=1
            if input[x][y] > 9 :
                input[x][y] = 0
                count +=1
                for b in get_neighbours((x,y)):
                    l,m = b
                    if input[l][m] > 0:
                        increase.append(b)    
        increase.pop(0)   
    return count
                            
                
                
steps=100
result = 0
for i in range(1,steps+1):
    glow = make_steps()
    result += glow
    
print("\n After step %s , there have been a total of %s flashes\n"% (steps,result))
 

print("\n-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime