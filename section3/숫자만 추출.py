import sys

sys.stdin = open('input.txt')

s = input()

int_s = ""

for c in s:
    if(c.isnumeric()):
        int_s+=c

n = int(int_s)

print(n)

cnt = 2
for i in range(2, n):
    if (n%i==0):
        cnt+=1
print(cnt)