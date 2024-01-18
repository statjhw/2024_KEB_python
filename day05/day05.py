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



while True :
    menu = input("""1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Is_Prime
                   4) Prime between two number   5)Quit Program : """)

    if menu == '1' :
        fahrenheit = float(input("input fahrenheit : "))
        print(f"Fahrenheit : {fahrenheit}, Celsius : {(fahrenheit - 32) * (5/9) : .4f}")
    elif menu == '2' :
        celsius = float(input("input celsius : "))
        print(f"Celsius : {celsius}, Fahrenheit : {celsius * (9/5) + 32 : .4f}")

    elif menu == '3' :
        number = int(input("Input number"))
        if isprime(number) :
            print(f'{number}는 소수입니다.')
        else:
            print(f'{number}는 소수가 아니다.')
    elif menu == '4' :
        lst_numbers = input("두 개의 숫자를 입력하세요 : ").split()

        n1 = int(lst_numbers[0])
        n2 = int(lst_numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1  # 파이썬에서 허용하는 swap 문법

        for number in range(n1, n2 + 1):
            if isprime(number) :
                print(number, end = ' ')
        print()

    elif menu == '5' :
        print("Quit Program")
        break;
    else :
        print('Ivalid Menu!')





