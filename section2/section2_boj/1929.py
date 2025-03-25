n, m = map(int, input().split())

arr = [i for i in range(0, m+1)]


# 1은 제외
arr[1] = 0

for i in range(2, m+1):
    if(arr[i]==0):
        continue
    
    for j in range(i*2, m+1, i):
        arr[j] = 0


ans = list(filter(lambda x : x>=n and x!=0, arr))

for a in ans:
    print(a)
