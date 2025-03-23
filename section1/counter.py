from collections import Counter

lst = list("yellowHello")

c = Counter(lst)

# Counter 객체 출력력
print(c) #Counter({'l': 4, 'e': 2, 'o': 2, 'y': 1, 'w': 1, 'H': 1})

#key들 뽑아내기
print(c.keys()) #dict_keys(['y', 'e', 'l', 'o', 'w', 'H'])

#values 뽑아내기
print(c.values()) #dict_values([1, 2, 4, 2, 1, 1])

#key로 value 뽑아내기 : dict와 동일
print(c['l'])

#value가 1인 key만 뽑아내기
lst = list(filter(lambda x: c[x]==1, c))
print(lst)

#value가 최소인 key 모두 뽑아내기
minLst = list(filter(lambda x: c[x]==min(c.values()), c))
print(minLst)