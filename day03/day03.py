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
blurt = "What the...!!?"
blurt.strip('.?!') #안에 들어가는 인자가 연속적으로 지워진다.
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
number = int(input("Input number : "))
count = 0
i = 2

while i < number :
    if number % i == 0 :
        count += 1
        break
    i += 1

if count == 0 :
    print(f"{number} is prime number")
else :
    print(f"{number} is not prime number")














