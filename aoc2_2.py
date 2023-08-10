with open('data/input2.txt') as f:
    lines = f.readlines()
    
list =[]

for e in lines:
    list.append(e.strip())
    
input = [words for segments in list for words in segments.split()]

hori = 0
dept = 0
aim  = 0

for i in range(0,len(input),2):
    if input[i] == 'forward':
        hori += int(input[i+1])
        dept += int(input[i+1])*aim 
    elif input[i] == 'down':
        aim += int(input[i+1])
    elif input[i] == 'up':
        aim -= int(input[i+1])
        
print("hori =", hori,
      "\ndept =", dept,
      "\nresult =",hori,"*",dept,"=",hori*dept)