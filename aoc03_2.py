b=12

with open('data/input3') as f:
    lines = f.readlines()
    
list =[]

for e in lines:
    list.append(e.strip())
    
input = [words for segments in list for words in segments]

input2 = []
input3 = []

for i in range(0,len(input),b):
    input2.append(input[i:i+b])        
    input3.append(input[i:i+b]) 


def getMostcommon(inputlist,x):
    
    zeroCount = 0
    oneCount  = 0 
    
    for i in range(0,len(inputlist)):
        
        if int(inputlist[i][x]) == 0:
            zeroCount += 1
        if int(inputlist[i][x]) == 1:
            oneCount += 1
            
    if zeroCount > oneCount:
        return 0
    else:
        return 1

      
def getLeastcommon(inputlist,x):
       
    zeroCount = 0
    oneCount  = 0 
    
    for i in range(0,len(inputlist)):
        
        if int(inputlist[i][x]) == 0:
            zeroCount += 1
        if int(inputlist[i][x]) == 1:
            oneCount += 1
            
    if zeroCount <= oneCount:
        return 0
    else:
        return 1


def getRat(list,com):

    for i in range(0,b):
        comp = com(list,i)
        j= 0
        
        while j < len(list):
            
            if len(list) == 1:
                    return list[0]
                
            if int(list[j][i]) != comp:
                list.pop(j)
                j -= 1
                
            j += 1       
                     
    return list[0]


oxyRat = getRat(input2,getMostcommon)  
co2Rat = getRat(input3,getLeastcommon)
        
def tooString(integers):
    
    strings = [str(integer) for integer in integers]
    return "".join(strings)

print("oxygen generator rating  = ",oxyRat,"=",int(tooString(oxyRat),2))
print("CO2 scrubber rating = ",co2Rat,"=",int(tooString(co2Rat),2))
print("result =",int(tooString(oxyRat),2),"*",int(tooString(co2Rat),2),"=",int(tooString(oxyRat),2)*int(tooString(co2Rat),2))