import sys
sys.stdin = open("input.txt")

from itertools import *


n, k = map(int, input().split())
arr = list(map(int, input().split()))

sums = set()

for comb in combinations(arr, 3):
    sums.add(sum(comb))


result = sorted(sums, reverse=True)
print(result[k-1])
