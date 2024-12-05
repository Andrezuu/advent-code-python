import heapq as pq
from collections import Counter

res=0
#with open("input", "r") as infile:
with open("test.txt", "r") as infile:
    for line in infile:
        nums = list(map(int, line.split()))
        isRemove = False
        isDecrease = 2
        didBreak = False
        i = 0
        j = 1
        print(nums)
        while i < len(nums) - 1:
            print(f'im i {i}, im j {j}')
            diff = abs(nums[i]-nums[j])
            if diff < 1 or diff > 3:
                didBreak = True
            if isDecrease== 2: 
                isDecrease = 1 if nums[i] > nums[j]  else 0
            if isDecrease == 1 and nums[i] < nums[j]:
                didBreak = True
            if isDecrease == 0 and nums[i] > nums[j]:
                didBreak = True
            if didBreak and not isRemove:
                isRemove = True
                i+=1
                j+=1
                didBreak = False
                continue
            if didBreak: break
            i+=1
            j+=1
        res+= 1 if not didBreak else 0
                        
            
            




print(res)
# with open("output1.txt", "w") as outfile:
    # outfile.write(f'my answer is {res}')





