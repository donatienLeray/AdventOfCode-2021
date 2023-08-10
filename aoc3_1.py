with open('data/input3.txt') as f:
    lines = f.readlines()
    
list =[]

for e in lines:
    list.append(e.strip())
    
input = [words for segments in list for words in segments]


gammal = []
epsilonl = []

def getMostcommon(x):
    
    zeroCount = 0
    oneCount  = 0 
    
    for i in range(x,len(input),12):
        
        if int(input[i]) == 0:
            zeroCount += 1
        if int(input[i]) == 1:
            oneCount += 1
            
    if zeroCount > oneCount:
        return 0
    else:
        return 1


for y in range(0,12):
     gammal.append(getMostcommon(y))
     

for i in gammal :
    if i == 0:
        epsilonl.append(1)
    else:
        epsilonl.append(0)
        
def tooString(integers):
    
    strings = [str(integer) for integer in integers]
    return "".join(strings)

gamma = tooString(gammal)
epsilon = tooString(epsilonl)

print("gamma   = ",gamma,"=",int(gamma,2))
print("epsilon = ",epsilon,"=",int(epsilon,2))
print("result =",int(gamma,2),"*",int(epsilon,2),"=",int(gamma,2)*int(epsilon,2))