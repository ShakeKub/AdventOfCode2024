import re
from collections import Counter
import sys

sys.setrecursionlimit(1000000)

ans = res = 0

def extract_numbers(line):
    return list(map(int, re.findall(r"-?\d+", line)))

with open("input.txt") as f:  
    s = f.read().strip()

ans = 0
left = []
right = []

for l in s.split("\n"):
    nums_list = extract_numbers(l)
    left.append(nums_list[0])
    right.append(nums_list[1])

left.sort()
right.sort()

ans = sum(abs(l_val - r_val) for l_val, r_val in zip(left, right))

#  PART TWO!!
#right_counter = Counter(right)

#ans = 0
#for left_value in left:
#    ans += left_value * right_counter[left_value]

print(ans)
