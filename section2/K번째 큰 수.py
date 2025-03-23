# import sys
# sys.stdin = open("input.txt")
n, k = map(int, input().split())


arr = list(map(int, input().split()))

arr.sort(reverse=True)

p1, p2, p3 = 0, 1, 2

results = []
cnt = 0

while True:
    if(p3==n):
        break
    cnt+=1
    sum = arr[p1] + arr[p2] + arr[p3]
    results.append(sum)

    if((p3+1)==n):
        if((p2+1)==(n-1)):
            p1+=1
            p2=p1+1
            p3=p2+1
        else:
            p2+=1
            p3 = p2+1
    else:
        p3+=1
        

results = list(set(results))
results.sort(reverse=True)
print(results[k-1])




