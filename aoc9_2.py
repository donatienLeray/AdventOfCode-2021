import time

start_time = time.time()  # just to time runtime
data = 'data/input9.txt'  # input filename

tmp = [10]                #tmp will be help array to read each line and they should all start with 10
input = []                #will hold oure line arrays

with open(data) as f:           #read in Data. the idea is to surround our original input 
  while True:                   #with 10s so we don't need to watch out for the edge cases 
    c = f.read(1)               #and can just compare evry original input with each neigbough
                                #since the edge cases are sourrounded with numbers that are higher in any case
    if not c:                   #read in char by char there arn't any left
        tmp.append(10)          #put a 10 in the end
        input.append(tmp)       #put the line araay in input input=[...,[10,...,10]]
        break                   #break since input ends
    if c == '\n':               #if line ends
        tmp.append(10)          # put a 10 at the end
        input.append(tmp)       #put the line araay in input input=[...,[10,...,10]]
        tmp = [10]              #put a 10in the begin of the next line
    else:                       #else make the char to int and add to line list
        tmp.append(int(c))

tmp1 = [10 for e in range(0,len(input[0]))]     #our goal is to get (x=input int):
input.append(tmp1)                              #[[10,10,...,10,10],
tmp2 = input                                    # [10,x,.....,x,10],
input= [tmp1]                                   # [10,x,.....,x,10],
                                                # [10,10,...,10,10]]
for e in tmp2:                                  #this part only puts the arrays of 10 in front 
    input.append(e)                             #and at the end so we get our wished form


def get_neighbours(e):                  #get all neigbouhs smaler than 9
    neighbours = []
    x,y = e
                                        #checks the value of all 4 neighbours
    if input[x-1][y] < 9 :              #if the value is smaöer than 9   
       neighbours.append((x-1,y))       #add the neighbouhg to list
    if input[x+1][y] < 9 :
       neighbours.append((x+1,y))
    if input[x][y-1] < 9 :
        neighbours.append((x,y-1))
    if input[x][y+1] < 9 :    
        neighbours.append((x,y+1))
    return neighbours                   #return list


def get_bassin(e):
    bassin=[]
    priority = [e]
    
    while len(priority) > 0 :
        f = priority[0]
        x,y = f
        
        if len(get_neighbours(f)) > 0:
            for a in get_neighbours(f):
                priority.append(a)
                       
        if input[x][y] < 9:
            input[x][y] = 10
            bassin.append(f)
        priority.pop(0)
        
    return bassin


lowpoints=[]

for i in range(1,len(input)-1):                     #no we itterate over our input ignoren the                  
    for j in range(1,len(input[i])-1):              #first and last row and colone
        a=input[i][j]                               #for each point we look if hes smaler than all his neighbours
        if input[i-1][j] > a and input[i+1][j] > a and  input[i][j-1] > a and input[i][j+1] > a :
            e = (i,j)
            lowpoints.append(e)                      #add the lowpint as coordinat tuple to the lowpoint list               


bassin_sizes=[]

for e in lowpoints:
    bassin_sizes.append(len(get_bassin(e)))
    
bassin_sizes.sort()
x = len(bassin_sizes)
print("\n result = ",bassin_sizes[x-1],"*",bassin_sizes[x-2],"*",bassin_sizes[x-3]," = ",bassin_sizes[x-1]*bassin_sizes[x-2]*bassin_sizes[x-3],"\n")


print("-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime