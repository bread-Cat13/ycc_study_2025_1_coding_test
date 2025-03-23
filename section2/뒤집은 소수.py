def reverse(x):
    str_x = str(x)
    new_str_x = ""
   
    for i in range(len(str_x)-1, -1, -1):
        new_str_x+=str_x[i]


    startIdx = -1
    for i in range(0, len(new_str_x)):
        if(new_str_x[i]!='0'):
            startIdx = i
            break
    
    new_str_x = new_str_x[startIdx:]

    return int(new_str_x)

def isPrime(x):
    if x==1:
        return False
    
    for i in range(2, x):
        if(x%i==0):
            return False
    
    return True

n = int(input())
nums = list(map(int, input().split()))

for n in nums:
    if(isPrime(reverse(n))):
        print(reverse(n), end=" ")