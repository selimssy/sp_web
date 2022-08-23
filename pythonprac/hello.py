a = 1
b = 2
print(a + b)    # 3


c = 'cats '
d = 'and dog'
print(c + d)    # cats and dog




a_list = ['사과', '배', '감']
print(a_list[0])    # 사과

a_list.append('수박')
print(a_list)  # ['사과', '배', '감', '수박']





a_dict = {
    'name' : 'bob',
    'age' : 27
}

print(a_dict['name'])    # bob







def sum(a, b):
   return a + b

result = sum(5, 3)
print(result)   # 8






def is_adult(age):
    if age >= 20:
        print('성인입니다')
    elif age > 13:
        print('청소년입니다')
    else:
        print('어린이입니다')

is_adult(17)    # 청소년입니다







#  과일 갯수 세기 함수
fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

classify = '배'
count = 0
for i in fruits:        # 파이썬 한 줄 for
    if i == classify:
        count += 1

print(count)    # 3







people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'], end='  ')    # bob  carry  john  smith  ben

print()   # 줄바꿈

for person in people:
    if person['age'] >= 20:
        print(person['name'], end='  ')   # bob  carry  ben