import sys

sys.stdin = open('kthNumber_input.txt')

t = int(input())

def returnKthNum(arr, start, end, k):
    # arr에서 start, end 끊어내기
    part = arr[start-1:end]
    part.sort()


    return part[k-1]

for i in range(t):
    N, s, e, k = map(int, input().split())
    target = list(map(int, input().split()))
    ans= returnKthNum(target, s, e, k)
    print("#{} {}".format(i+1, ans))