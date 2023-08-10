import time

start_time = time.time()  # just to time runtime
data = 'data/input10.txt'  # input filename

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
        tmp.append(c)
          
result = []

opposit = {'(' : ')', '{' : '}', '[' : ']', '<' : '>', ')' : '(', '}' : '{', ']' : '[', '>' : '<' }

points = { ')' : 3, '}' : 1197, ']' : 57, '>' : 25137 }

def is_corrupted(i):
    stack = []
    
    for e in input[i]:
        if e in ['(','{','[','<'] :
            stack.append(e)
            
        if e in [')','}',']','>'] :
            if not stack[-1] == opposit.get(e) :
                print("Expected ",opposit.get(stack[-1]),",but found",e, " in line ",i)
                result.append(points.get(e)) 
                break
            else:
                stack.pop(-1)  
                              
    return stack
    
    
for i in range(0,len(input)):           
   is_corrupted(i)  
   
print("\nresult = ",sum(result),"\n")
        
print("\n-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime