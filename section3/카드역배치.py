# import sys

# sys.stdin = open('input.txt')

lst = [i for i in range(0, 21)]

for i in range(10):
    a, b = map(int, input().split())
    lst = lst[:a] + lst[b:a-1:-1] + lst[b+1:]


for e in lst:
    if e==0:
        continue
    print(e, end = ' ')