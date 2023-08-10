import time
import re

start_time = time.time()  # just to time runtime

data = 'data/input12.txt'  # input filename

with open(data) as f:
    lines = f.readlines()
 
line = [e for e in lines] 
list = [re.split('\-|\n| ',e) for e in line]
list =  [item for sublist in list for item in sublist] 
input  = [x for x in list if x != '' ]


def make_graph():
    graph = {}
    for i in range(0,len(input),2):
        x = input[i]
        y = input[i+1]
        if not x in graph.keys():
            graph.update({x:[y]})
        if not y in graph.keys():
            graph.update({y:[x]})
        if x in graph.keys():
            tmp= graph.get(x)
            if not y in tmp:
                tmp.append(y)
            graph.update({x : tmp })
        if y in graph.keys():
            tmp= graph.get(y)
            if not x in tmp:
                tmp.append(x)
            graph.update({y : tmp })
    return graph
        
graph = make_graph()
    
paths = []

def find_paths(root):
    if root[-1] == 'end':
        paths.append(root)
        return
    for e in graph.get(root[-1]):
        if e.isupper():
            copy = root.copy()
            copy.append(e)
            find_paths(copy)
        if e.islower():
            if not e in root:
                copy = root.copy()
                copy.append(e)
                find_paths(copy)

find_paths(['start']) 


print("\nthere are %s paths through the cave system" % len(paths))

        
print("\n-------- %s seconds --------" % (time.time() - start_time),"\n") #print runtime