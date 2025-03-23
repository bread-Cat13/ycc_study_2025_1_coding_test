# import sys
# sys.stdin = open('input.txt')

def returnPrimeNums(n):
    # 0, 1은 들어있지만 무시해야 함
    arr = [i for i in range(n+1)]
    arr[1] = 0
    
    for i in range(2, n+1):
        if(arr[i]==0):
            continue

        for j in range(i*2, n+1, i):
            arr[j] = 0
    
    return len(list(filter(lambda x: x!=0, arr)))

    


n = int(input())

print(returnPrimeNums(n))


