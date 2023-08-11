import time
import re
from collections import Counter

start_time = time.time() # just to time runtime
data = 'data/test8.txt'  # input filename

with open(data) as f:           
    lines = f.readlines()     # read file
 
list = [re.split('\||\n',e) for e in lines]            # split by '|' and \n    
list =  [item for sublist in list for item in sublist] # make 2D list to 1D list

input=[]
output=[]

for i in range(0,len(list),3):       # list is now ['input','','output','in...] so steps are 3
    input.append(list[i].split())    # get the input from list smd seperades the strings by ' '   
    output.append(list[i+1].split()) # same with output


def most_Common(lst):                # methode to get most common from list
    data = Counter(lst)              # from https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
    return data.most_common(1)[0][0]

def decode_a():                                # find segment a by substracting the two segment from 1 of 7
    a = numbers[7].replace(numbers[1][0],'')   #  (7-1=a)
    decode[0]= a.replace(numbers[1][1],'')
    
def decode_bef(index,len):                                     # if a segmant has an uniq count 
    bef = [name for name, age in signal.items() if age == len] # you can fint it by looking up the cound in signal
    decode[index] = bef[0]                                     
      
def decode_c():
    ac = [name for name, age in signal.items() if age == 8]
    ac.remove(decode[0])
    decode[2] = ac[0]
 
def decode_dg():
    dg = [i for x in len_6 for i in x]  # in the list of all inputs signals with length 6
    for i in decode:                    # we know every segment exept d and g
        while i in dg:                  # so if we remoove everything we are left with a list of d an g
            dg.remove(i)
    decode[6] = most_Common(dg)         # thanks to some logic we know g comes up the most often (3times)
    while decode[6] in dg:              
            dg.remove(decode[6])        # now we can remoove all (g)s from the list 
    decode[3]= dg[0]                    # we are left with d
            


def  decode_line(line_nr):
    for j in input[line_nr] :  # filter out all numbers with uniqe length
        if len(j) == 2 :
            numbers[1] = j
        if len(j) == 4 :
            numbers[4] = j
        if len(j) == 3 :
            numbers[7] = j
        if len(j) == 7 :
            numbers[8] = j
        if len(j) == 6 :      # make a list of the 3 numbers with lentgth 6
            len_6.append(j)   # neede for decode d and g
        for k in j :
            signal[k] += 1    # maps how often a specific segment comes up (used in decode_bef and decode_c ) 
            
    decode_a()           #decode a
    decode_bef(1,6)      #decode b
    decode_c()           #decode c
    decode_bef(4,4)      #decode e
    decode_bef(5,9)      #decode f
    decode_dg()          #decode d and g
              

    #now we know all segments we can find the code for all reamining numbers
    numbers[0] = decode[0] + decode[1] + decode[2] + decode[4] + decode[5] + decode[6]
    numbers[2] = decode[0] + decode[2] + decode[3] + decode[4] + decode[6]
    numbers[3] = decode[0] + decode[2] + decode[3] + decode[5] + decode[6]
    numbers[5] = decode[0] + decode[1] + decode[3] + decode[5] + decode[6]
    numbers[6] = decode[0] + decode[1] + decode[3] + decode[4] + decode[5] + decode[6]
    numbers[9] = decode[0] + decode[1] + decode[2] + decode[3] + decode[5] + decode[6]
 
    
result = 0
for i in range(0,len(input)): #line by line                                  
    decode =['','','','','','','']                                   # list of the decoded segments where index(0,1,...) = a,b ...
    numbers = ['','','','','','','','','','']                        # list of the decoded nubers where index = number
    signal= {'a':0, 'b' :0, 'c' :0, 'd' :0, 'e' :0, 'f' :0, 'g' :0}  # list of how often that segment came up in input 
    len_6 = []
    decode_line(i)                                                   # this funktion fills out all list correctly
    test_out = ["".join(sorted(i)) for i in output[i]]               # sort the output number-strings to be bale to find them
    numbers = ["".join(sorted(i)) for i in numbers]                  # sort our the decoded number-strings for easy compare
    resultlist = [str(numbers.index(i)) for i in test_out]           # find outputvalue in our decoded nubers map them to index
    line_result = int(''.join(resultlist))                           # join reult list to get int value
    print("line",i ,"result =",line_result)
    result += line_result                                            # add line result to current result

print("---------------------------------")
print("result =",result)                                             # print sums of all line results as final result
print("---------------------------------")
print("-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime