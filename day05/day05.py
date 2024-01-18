#딕셔너리 축약어
#
# words = 'letters'
# letter_counts = {letter : words.count(letter) for letter in words}
# print(letter_counts)

#for문으로 변경
# univ = 'inha university'
# count_alpha = dict()
# for letter in univ :
#     count_alpha[letter] = univ.count(letter)
# print(count_alpha)

#set
#딕셔너리에서 key들만 담는 데이터 타입이다.
#딕셔너리를 집합으로 만들 때는 키 값들만 가져온다.
#순서가 없다.

#조합과 연산
#& -> 교집합이 존재하면 true를 반환한다. intersection
# | 합집합 union
#차집합 -> difference
#^ -> 합집합에서 교집합을 뺀 집합
#imutable한 set ->frozen set


#함수
def isprime(n) -> bool: #리턴 type이 bool이라고 선언
    '''
    매개변수로 넘겨 받은 수가 소수인지를 여부를 boolean type으로 return
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    '''     #함수에 대한 설명

    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n :
            if n % i == 0 :
                return False
            i += 1
        return True


# help(isprime)
#
#
# lst_numbers = input("두 개의 숫자를 입력하세요 : ").split()
#
# n1 = int(lst_numbers[0])
# n2 = int(lst_numbers[1])
#
# if n1 > n2:
#     n1, n2 = n2, n1  # 파이썬에서 허용하는 swap 문법
#
# for number in range(n1, n2 + 1):
#     if isprime(number) == True:
#          print(number, end=' ')


#
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
#         if isprime(number) :
#             print(f'{number}는 소수입니다.')
#         else:
#             print(f'{number}는 소수가 아니다.')
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
#             if isprime(number) :
#                 print(number, end = ' ')
#         print()
#
#     elif menu == '5' :
#         print("Quit Program")
#         break;
#     else :
#         print('Ivalid Menu!')


#인수와 매개변수
#none
#none 과 boolean을 구분하기 위해서 is를 사용한다.

#Argument
#1. 위치 인수
#2. 키워드 인수 위치 인수가 먼저 와야한다.

#dufalut 매개변수에 생성된 데이터는 메모리에 남는다.

#ex)
# >>> def buggy(arg, result=[]): ... result.append(arg) ... print(result)
# ...
# >>> buggy('a')
# ['a']
# >>> buggy('b') # expect ['b'] ['a', 'b']
#none을 이용하면 원본이 복사되는 경우를 해결할 수 잇다.
#is none을 이용해서 경우에 따라서 선택가능
# >>> def nonbuggy(arg, result=None):
# ... if result is None:
# ... result = []
# ... result.append(arg)
# ... print(result) ...
# >>> nonbuggy('a') ['a']
# >>> nonbuggy('b')


# * 가변 인수들을 튜플로 담는다. 위치 인수 뒤에 나와야 한다.
# 파이썬 함수 오버로당

#경우1 
# def a(n) :
#     return n
# def a(n1, n2) :
#     return n1 + n2
#
# print(a(1 , 2))
# print(a(1))

#경우2 : 줄 순서가 앞에 있는 경우
# def a(n1, n2) :
#     return n1 +n2
# def a(n) :
#     return n
# print(a(1+3))
# print(a(1,3))
# print(a(1+3))
#함수가 먼저 오는 것에 상관없음


#* 가변 인수 : 튜플에 담기고
# ** 가번 인수 : 딕셔너리에 담긴다.
#인수의 순서 : 1. 위치 인수, optional 인수, optional keyword 인수
#keyword only Arguments

#mutable/immutable -> 함수를 인수로 받을 때
#mutable -> pass by refernce방식
#imutable ->

#help문 보는 법
#print(func_name.__doc__)
#print(max.__doc__)


#모든 테이터 타입이 객체이므로 인수로 사용할 수 있다.
#함수를 return할 수 있다.

#Functions Are First-Class Citizens
#ex
# def squares(n) :
#     return n*n

# def run_func(func,*n) -> list:
#     return func(*n)
#
#
# #가변매개변수 매개변수가 몇개 올지 모를 때
# def sum_arg(*arg) :
#     return sum(arg)
#
# def squares(*n) -> list:
#     '''
#     넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
#     :param n: tuple
#     :return: list
#     '''
#     return [i**2 for i in n]
#
# print(squares(9, 5, 2))
# print(run_func(squares, 9, 10))

#inner function
# def outer(a, b) :
#     def inner(c, d) :
#         return c + d

#closures
#상위 함수의 매개변수를 그대로 사용할 수 있다.
#함수 자체를 리턴으로 한다. #함수 클래스다.
#클로저를 이용해 변수를 지정하면 변수는 함수의 메모리 주소를 가진다.
#아예 새로운 함수를 생성?
#메모리 주소가 다르다.


# def a() :
#     return n
#
# print(a)

#map함수
# numbers = ["7", "-11", "3"]
# print(sum(map(int, numbers)))

# def squares(n) :
#     return n * n
#
# even_number = [i for i in range(51) if i % 2 == 0]
# print(even_number)
# print(map(squares, even_number))
# print(list(map(lambda x : x**2, even_number)))
#
# z = lambda x :pow(x, z)
# z(4)

#generator
#sequence 객체 ->
#generator
#직접 함수 구현 -> yield 직접 던지고 다시 코드로 돌아간다.

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

#r
r = my_range()
print(r, type(r))
for  x in r :
    print(x)

#한번 사용 후 지워진다.

#Decorators
#수정이 아니라 함수에 추가하고 싶은 것이 있을 때 사용한다.

#정의 함수 위에 @Decorators 표현을 사용해서 함수를 사용한다.
#v5.1 - commit









