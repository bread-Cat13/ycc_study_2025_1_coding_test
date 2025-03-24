import sys
sys.stdin = open('input.txt')


n = int(input())
results = list(map(int, input().split()))


#n=1인 경우
if(n==1):
    print(results[0])
else:
    score, cur = 0, 1
    x, y = 0, 1

    while(x<n):
        if(results[x]==1):
            score+=cur
            if(x!=n-1):
                if(results[y]==0):
                    cur = 1
                else:
                    cur += 1
        
        x+=1
        y+=1
    
    print(score)




