#과제 리뷰
# while True :
#     menu = input("""1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Is_Prime
#                    4) Prime between two number   5)Quit Program : """)
#
#     if menu == '1' :
#         fahrenheit = float(input("input fahrenheit : "))
#         print(f"Fahrenheit : {fahrenheit}, Celsius : {(fahrenheit - 32) * (5/9) : .4f}")
#     elif menu == '2' :
#         celsius = float(input("input celsius : "))
#         print(f"Celsius : {celsius}, Fahrenheit : {celsius * (9/5) + 32 : .4f}")
#
#     elif menu == '3' :
#         number = int(input("Input number"))
#         is_prime = True
#
#         if number < 2:
#             print(f"{number}는 소수가 아니다.")
#         else:
#             for i in range(2, number) :
#                 if number % i == 0 :
#                     is_prime = False
#                     break;
#
#             if is_prime:
#                 print(f'{number}는 소수입니다.')
#             else:
#                 print(f'{number}는 소수가 아니다.')
#     elif menu == '4' :
#         lst_numbers = input("두 개의 숫자를 입력하세요 : ").split()
#
#         n1 = int(lst_numbers[0])
#         n2 = int(lst_numbers[1])
#
#         if n1 > n2:
#             n1, n2 = n2, n1  # 파이썬에서 허용하는 swap 문법
#
#         for number in range(n1, n2 + 1):
#             is_prime = True
#
#             if number < 2:
#                 continue
#             else:
#                 for i in range(2, number):
#                     if number % i == 0:
#                         is_prime = False
#                         break
#                 if is_prime == True:
#                     print(number, end=' ')
#         print()
#     elif menu == '5' :
#         print("Quit Program")
#         break;
#     else :
#         print('Ivalid Menu!')


#4번 menu 리뷰
# lst_numbers = input("두 개의 숫자를 입력하세요 : ").split()
#
# n1 = int(lst_numbers[0])
# n2 = int(lst_numbers[1])
#
# if n1 > n2:
#     n1, n2 = n2, n1  # 파이썬에서 허용하는 swap 문법
#
# for number in range(n1, n2 + 1):
#     is_prime = True
#
#     if number < 2:
#         continue
#     else:
#         i = 2
#         while i*i <= number :    #소수의 특성을 이용
#             if number % i == 0:
#                 is_prime = False
#                 break
#             i += 1
#
#         if is_prime == True:
#             print(number, end=' ')


#튜플
#,를 이용해서 생성 -> ()는 옵션

t6 = 'python', 'pythonc++' #packing
# print(type(t6), print(t6[0]))
#
# subject, prof = t6
# print(prof) #unpacking
# print(subject)
#
# t7 = () #빈소괄호는 튜블로 저장
# t8 = tuple()
# print(type(map(str, t6)))   #map은 클래스로 저장
# a, b =map(str, t6)
# print(a, b)

#packing과 unpacking을 이용한 swap
# t9 = 1, 2, 3
# t10 = 1, 2
# print(t9 == t10)

#비교 연산자는 튜플 원소의 순서대로 비교한다.

#for문 이용 시 시퀀스 자료 사용 -> in

#튜플 수정 시 새로운 객체를 만든다.
# id() 객체의 메모리 주소를 출력한다.
# t1 = 1,2,3
# print(id(t1))
# t2 = 4,5
# t1 += t2
# print(id(t2))
#왜냐하면 immutable하기 때문에 새로운 객체를 만들어서 사용한다.

#리스트
#슬라이싱
#단계만 음수로 지정 시 뒤에서 부터 슬라이싱
# subject = ['C++', 'java', 'python']
# print(subject[::-1])
# subject.reverse()   #reverse()함수는 원본을 바꾼다.
# print(subject)

#append() O(1)의 시간복잡도를 가진다.
#insert() O(n)의 시간복잡도를 가진다.

#리스트 결합 expend(), +=, *append()
#append()는 리스트 안에 리스트를 넣는다.

#리스트 슬라이싱을 이용한 값 할당
#우변에 문자열이 오는 경우 -> 리스트로 변경된 후 리스트에 저장된다.(문자열의 크기와 슬라이싱의 갯수가 같아야 한다.)

#리스트 삭제
#del함수 이용
#Delete an Item by Value with remove() #같은 값이 여러 개 있는 경우에는 제일 앞에 있는 것만 지운다.
#pop 마지막 원소만 지운다.

#in
#count갯수
#join 리스트 -> 문자열로 결합


#정렬
#1. sort() -> 원본을 바꾼다. *option reverse=True 뒤부터 정렬
# 여러 개의 데이터 타입을 비교 불가능
# 문자열 안에서는 숫자 문자열, 영문 문자열, 한글 문자열 순으로 오름차순 정렬된다.


#2 sorted() -> 복사해서 사용한다.

#갯수
# len()

#복사 (얇은복사/깊은복사)
#1 얇은복사
# subject = ['a', 'b', 'c']
# a = subject
# b = a.copy()
# c = list(subject)
# print(subject, a,b,c)
# subject[1] = 'x'
# print(subject, a,b,c)


#2 깊은 복사 (리스트 안에 mutable한 자료가 있을 때)
# subject = ['a', ['c','b'], 'd']
# a = subject
# b = a.copy()
# c = list(subject)
# print(subject, a,b,c)
# subject[1][1] = 'x'
# print(subject, a,b,c)


# import copy
# subject = ['a', ['c','b'], 'd']
# a = subject
# b = copy.deepcopy(a)
# subject[1][1] = 'x'
# print(a,b)


#zip()함수 : 여러 개의 시퀀스를 만들어 주기 위해서이다.
# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# # drinks = ['coffee', 'tea', 'beer']
# # desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
# # for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
# #     print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
#
#
# print(list(zip(days, fruits)))
# print(dict(zip(days, fruits)))
#
# #Create a List with a Comprehension
# numbers_list1 = list(range(1,6))
# numbers_list2 = [number for number in range(1,6)] #[expression for item in iterable]
# print(numbers_list1, numbers_list2, sep = '\n')
#
# #제곱 수
# print([number**2 for number in numbers_list1])
# #조건 문이 들어갈 수 있다.
# print([number**2 for number in numbers_list1 if number % 2 == 0])
# #
# rows = range(1,4)
# cols = range(1,3)
# cells = [(row, col) for row in rows for col in cols]
# for cell in cells :
#     print(cell)
# for row, col in cells :
#     print(row, col)
#
#
#
# #튜플과 리스트의 차이점
#
# #딕셔너리
#
# #value에 접근하는 법
# #1. 대괄호
# #2. get함수 이용
# #2번째 인수는 해당 키가 없으면 출력할 메세지를 받는다.
#
#
# sugang = dict(python="kim", cpp ="sung", db="kang")
# print(sugang)
# sugang['datastructure'] = 'kim'
# sugang['datastructure'] = 'park'    #update
#
# print(sugang)
# print(sugang['python'])
#
# print(sugang.get('opensource', 'no opensource'))
# sugang = dict(python="kim", cpp ="sung", db="kang")
# for subject, prof in sugang.items() :
#     print(f"{subject} 과목 담당 교수 : {prof}입니다." )
#
# print(sugang.items())

#
drinks_food = {'위스키' : '초콜릿', '와인' : '치즈', '소주' : '삼겹살', '고량주' : '양꼬치'}
drink = input(f"{' , '.join(list(drinks_food.keys()))} 중에서 고르시오")
drinks_food_keys = list(drinks_food.keys())
while True :
    menu = input(f"{' , '.join(list(drinks_food.keys()))} 중에서 고르시오")
    if menu == '1' :
        print(f"{drinks_food_keys[0]}에 어울리는 안주는 {drinks_food[drinks_food_keys[0]]}")
    elif menu == '2' :
        print(f"{drinks_food_keys[1]}에 어울리는 안주는 {drinks_food[drinks_food_keys[1]]}")
    elif menu == '3' :
        print(f"{drinks_food_keys[2]}에 어울리는 안주는 {drinks_food[drinks_food_keys[2]]}")
    elif menu == '4' :
        print(f"{drinks_food_keys[3]}에 어울리는 안주는 {drinks_food[drinks_food_keys[3]]}")
    elif menu == '5' :
        print("다음에 또 오시오")
        break










