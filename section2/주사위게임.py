import sys
sys.stdin = open('input.txt')

from collections import Counter

def calPrize(lst):

    c = Counter(lst)

    length = len(c)
    
    if length == 3:
        return max(lst)*100
    elif length ==2:
        target = list(filter(lambda x: c[x]==2, c))[0]
        return 1000 + target*100
    else:
        return 10000 + lst[0]*1000




n = int(input())

prizeLst = []

for i in range(n):
    prizeLst.append(calPrize(list(map(int, input().split()))))

print(max(prizeLst))

