# def plus_one(x):
#     return x+1

# print(plus_one(1))


# lambda [매개변수]: [return식] => 당연히 변수에 할당 필요 => 이때 변수가 함수명이 됨

#예시시
plus_two = lambda x: x+2
test = lambda x,y: x+y



#내장함수에 유리
#예) map(적용함수, 자료구조) -> 적용함수에 람다식으로 작성 가능!
a = [1,2,3]
new_a = list(map(plus_two, a)) # 함수사용 

print(new_a)


aplus3 = list(map(lambda x: x+3, a)) # 람다사용
print(aplus3)


#sort 내장함수에도 람다함수를 사용 for 정렬 함수 지정



