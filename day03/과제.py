#python day3 과제

#과제 1
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
#
#         is_prime = True
#         if number < 2:
#             print(f"{number}는 소수가 아니다.")
#         else:
#             for i in range(2, number):
#                 if number % i == 0:
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


#과제2
#1
# lst = list = [3, 2, 1, 0]
# for i in range(len(lst)) :
#     print(lst[i])
#
#
# #2
# guess_me = 7
# number = 1
# while True :
#     if number < guess_me :
#         print(f"{number} is too low")
#
#     elif number == guess_me :
#         print(f"found it! number is {number}")
#         break
#     elif number > guess_me :
#         print("oops")
#         break
#     number += 1


#3
# guess_me = 5
#
# for number in range(10) :
#     if number < guess_me :
#         print(f"{number} is too low")
#
#     elif number == guess_me :
#         print(f"found it! number is {number}")
#         break
#     elif number > guess_me :
#         print("oops")
#         break








