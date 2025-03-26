import sys

sys.stdin = open('input.txt')


def isReverseString(s):
    flag = True
    s = s.lower()

    for i in range(int(len(s)/2)):
        if(s[i]!=s[len(s)-i-1]):
            return "NO"
    
    return "YES"

n = int(input())

for i in range(1, n+1):
    print('#{} {}'.format(i, isReverseString(input())))


