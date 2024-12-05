
import re
res=0
#with open("input", "r") as infile:
with open("test.txt", "r") as infile:
    res= 0 
    for line in infile:
        # x  = map(lambda tup: (int(tup[0]), int(tup[1])), re.findall(r"do\(\)|don't\(\)|mul\(([0-9]+),([0-9]+)\)":, line))
        x  = re.findall(r"(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)", line)
        #dos  = re.findall(r"do\(\)|don't\(\)", line)
        print(x)
    print(res)
                        
            
            




