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
lst_numbers = input("두 개의 숫자를 입력하세요 : ").split()

n1 = int(lst_numbers[0])
n2 = int(lst_numbers[1])

if n1 > n2:
    n1, n2 = n2, n1  # 파이썬에서 허용하는 swap 문법

for number in range(n1, n2 + 1):
    is_prime = True

    if number < 2:
        continue
    else:
        i = 2
        while i*i < number :
            if number % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime == True:
            print(number, end=' ')
































