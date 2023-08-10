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


opposit = { '(' : ')', '{' : '}', '[' : ']', '<' : '>', ')' : '(', '}' : '{', ']' : '[', '>' : '<' }

points = { ')' : 1, '}' : 3, ']' : 2, '>' : 4 }

scores = []

def is_corrupted(i):
    stack = []
    completer = []
    
    for e in input[i]:
        if e in ['(','{','[','<'] :
            stack.append(e)
            
        if e in [')','}',']','>']:
            if not stack[-1] == opposit.get(e) :
                return None
            else:
                stack.pop(-1)
                
    for x in stack:
        completer.append(opposit.get(x))
        
    completer.reverse()
    return completer      
    
    
def calc_score(x) :
    score = 0
    for i in x:
        score = score*5
        score += points.get(i)
    scores.append(score)
    
         
for i in range(0,len(input)):
   x= is_corrupted(i)           
   if x:
       calc_score(x) 

scores.sort()
print(scores)
print("result = ",scores[int((len(scores) - 1)/2)])
        
print("\n-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime