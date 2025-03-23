# import sys
# sys.stdin = open("input.txt")

def digit_sum(x):
    num_str = str(x)
    result = 0
    for c in num_str:
        result += int(c)
    
    return result

n = int(input())
nums = list(map(int, input().split()))

sums = [digit_sum(n) for n in nums]

i = sums.index(max(sums))
print(nums[i])
