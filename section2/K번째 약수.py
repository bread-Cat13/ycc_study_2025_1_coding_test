n,k = map(int, input().split())

#  1,2,3,6 
#k=3,2,1

for i in range(1, n+1):
    if(k==1):
        if(n%i==0):
            ans = i
            break
    else:
        if(n%i==0):
            k-=1


print(ans if k==1 else -1)


# 다른 풀이
# cnt = 0
# for i in range(1, n+1):
#     if(n%i==0):
#         cnt +=1
#     if(cnt==k):
#         print(i)
#         break

# print(-1)
