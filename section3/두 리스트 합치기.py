# import sys

# sys.stdin = open('input.txt')

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))


n_ptr, m_ptr = 0, 0
sorted_lst = []

while(n_ptr<n and m_ptr<m):
    if(arr_n[n_ptr]<=arr_m[m_ptr]):
        sorted_lst.append(arr_n[n_ptr])
        n_ptr+=1
    else:
        sorted_lst.append(arr_m[m_ptr])
        m_ptr+=1


while(n_ptr<n):
    sorted_lst.append(arr_n[n_ptr])
    n_ptr+=1

while(m_ptr<m):
    sorted_lst.append(arr_m[m_ptr])
    m_ptr+=1


for e in sorted_lst:
    print(e, end = ' ')
