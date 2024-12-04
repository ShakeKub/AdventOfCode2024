import re
import sys

sys.setrecursionlimit(1000000)

ans = 0

def extract_numbers(line):
    return list(map(int, re.findall(r"-?\d+", line)))

with open("input.txt") as f:  
    s = f.read().strip()

for line in s.split("\n"):
    nums_list = extract_numbers(line)
    g = (
        all(a > b for a, b in zip(nums_list, nums_list[1:])) or
        all(a < b for a, b in zip(nums_list, nums_list[1:]))
    )
    
    if g:
        nums_list.sort()  
        for a, b in zip(nums_list, nums_list[1:]): 
            if b - a > 3 or b - a < 1:
                g = False
                break
        
        if g:  
            ans += 1

# PART TWO 
#def check(sequence):
#    g = (
#        all(a > b for a, b in zip(sequence, sequence[1:])) or
#        all(a < b for a, b in zip(sequence, sequence[1:]))
#    )
#    
#    if g:
#        sequence.sort()
#        for a, b in zip(sequence, sequence[1:]):  
#            if b - a > 3 or b - a < 1:
#                g = False
#                break
#    return g
#
#with open("input.txt") as f:  
#    s = f.read().strip()
#
#for line in s.split("\n"):
#    nums_list = extract_numbers(line)
#
#    if check(nums_list) or any(check(nums_list[:i] + nums_list[i+1:]) for i in range(len(nums_list))):
#        ans += 1
print(ans)
