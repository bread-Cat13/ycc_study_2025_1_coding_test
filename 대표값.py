# import sys, math
# sys.stdin = open("input.txt")


def getMinIdxOfMaxValuesFromDict(dict):
    max_value = max(list(dict.values()))
    returnLst=[]
    for k,v in dict.items():
        if v==max_value:
            returnLst.append(k)
    return min(returnLst)


n = int(input())
arr = list(map(int, input().split()))

mean = int(round(sum(arr)/n, 0))

gap = [abs(e-mean) for e in arr]


min_dict = dict()

for i in range(len(gap)):
    if(gap[i]==min(gap)):
        min_dict[i] = arr[i]

print(mean, getMinIdxOfMaxValuesFromDict(min_dict)+1)




