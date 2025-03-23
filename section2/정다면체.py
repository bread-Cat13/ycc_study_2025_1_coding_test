# import sys
# sys.stdin = open('input.txt')
from collections import Counter

n, m = map(int, input().split())


sum_lst = []

for i in range(1, n+1):
    for j in range(1, m+1):
        sum_lst.append(i+j)

c = Counter(sum_lst)

def getKeysOfMaxValues(c):
    lst =[]
    maxV = max(c.values())

    for e in c:
        if c[e] == maxV:
            lst.append(e)
    return lst
lst = getKeysOfMaxValues(c)
lst.sort()
for l in lst:
    print(l, end=" ")
