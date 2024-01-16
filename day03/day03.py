#raw string #탈출문자를 바로 보여주기 위해서
# university = r"Inha\nunicersity"
# print(university)
#
# #combine string
# num1 = input()
# num2 = input()

#print(num1 + num2)

#문자열에 *가능하다.
#할당은 안되지만 인덱싱은 가능하다.
#역방향인덱싱 [-1]은 맨 마지막 값을 리턴한다.

#할당은 되지 않지만 replace함수를 대신해 사용한다.
# a = 'penny'
# b = a
# a = a.replace('p','h')
# print(a, b)
#
# university = "Inha\nunicersity"
# print(university[:4])
# print(university[:-11])
# #len(문자열): 문자열의 갯수를 리턴해 준다.
#
# #split 문자열을 분리해서 리스트에 담는다.
# course = "2024 KEB bootcamp"
# print(course.split()) #구분자는 삭제해서 리스트에 저장한다.
#
# numbers = input("FirstNumber SecondNumber").split()
# print(int(numbers[0]) + int(numbers[1]))
#
#str.split
# #join
# #리스트를 문자열로 만들어준다.
# list_subjects = ['python', 'c++', 'database']
# str_subjects = ' / '.join(list_subjects)
#
# #replace
# print(course.replace('KEB', 'Inha'))
# #changing up to 100 of them(최대 100개 까지 대체한다.)
# print(course.replace('KEB', 'Inha',100))

#strip() 필요없는 문자열 제거
#lstrip <-left공간을 지운다.
#rstrip <-right공간을 지운다.
#구분자를 설정 가능하다.
#연속적으로 있어야 한다.
# blurt = "What the...!!?"
# blurt.strip('.?!') #안에 들어가는 인자가 연속적으로 지워진다.
#연속적으로 있는 앙쪽 끝을 제거?

#startswith, endswith true와 false로 return

#find 찾고자 하는 문자열의 위치를 반환하다.
#rfind는 뒤에서부터 찾는다. #reverse find
#찾고자하는 문저열이 없다면 find는 -1 반환, index는 ValuEerror발생

#예외처러로
# subjects = 'python c++ database linux'
# sub = input()
#
# try :
#     print(f"햐당 과목이 존재합니다. 위치는 {subjects.index(sub)}번 인덱스입니다.")
# except ValueError :
#     print("해당 과목이 존재하지 않습니다.")
#
# #count함수
#문자열 안에 인수문자열이 몇개인지를 반환한다.

#isalnum함수
#문자열을 구성하는 값들이 수치형과 문자열으로 이루어져 있는지

#영문의 소문자와 대문자를 바뀌주는 함수

#함수를 정렬하는 함수
#center, ljust(), rjust(), 문자열 출력 시 사용

#포멧팅
#'%d%%' % 100

#'%+(-)12d'#왼쪽, 오른쪽을 기준으로 정렬
#%.3은 소숫점 자릿수

#formating
# subjects =  {'python' : 'kin', 'c++' : 'sung', 'datastucture' : 'kim'}
# print("{0[python]}, {0[datastucture]}".format(subjects))



#소수
# number = int(input("Input number : "))
# is_prime = True
# i = 2
# if number < 2:
#     print(f'{number} is not prime number!')
# else :
#     while i < number :
#         if number % i == 0 :
#             is_prime = False
#             break
#         i += 1
#
# if is_prime :
#     print(f"{number} is prime number")
# else :
#     print(f"{number} is not prime number")

# univ = "inha"
#
# for k in range(0, len(univ),1) :
#     print(univ[k], end = '')
# #default start = 0
#
# number = int(input("Input number:"))
#
# if number < 2:
#     print(f'{number} is not prime number!')
# else :
#     for i in range(2, number) :
#         if number % i == 0 :
#             is_prime = False
#             break
#         i += 1
# if is_prime :
#     print(f"{number} is prime number")
# else :
#     print(f"{number} is not prime number")


#while과 for문에 붙는 else는 break가 되지 않으면 실행된다.
#range는 리스트에 담아서 봐야한다.
#역순으로 가려면 단계인자를 -로 지정

# numbers = input("Input two number :").split()
# n1 = int(numbers[0])
# n2 = int(numbers[1])
#
# if n1 > n2 :
#     n1 , n2 = n2, n1 #파이썬에서 swap없이 수를 swap하는 방법
#
# for number in range(n1, n2+1) :
#     is_prime = True
#
#     if number < 2:
#         continue
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime :
#             print(number, end = ' ')


# name = 'inha'
# print(name[-3:-1])


# number = int(input("Input number"))
#
# is_prime = True
# if number < 2 :
#     print(f"{number}는 소수가 아니다.")
# else :
#     for i in range(2, number) :
#         if number % i == 0 :
#             is_prime = False
#             break;
#
#     if is_prime :
#         print(f'{number}는 소수입니다.')
#     else :
#         print(f'{number}는 소수가 아니다.')


lst_numbers = input("두 개의 숫자를 입력하세요 : ").split()

n1 = int(lst_numbers[0])
n2 = int(lst_numbers[1])

if n1 > n2 :
    n1, n2 = n2, n1

for number in range(n1, n2+1) :
    is_prime = True

    if number < 2 :
        continue
    else :
        for i in range(2, number) :
            if number % i == 0 :
                is_prime = False
                break
        if is_prime == True :
            print(number, end = ' ')

























