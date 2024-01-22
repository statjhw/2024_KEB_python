#class 속성
#클래스의 속성을 객체가 받는다. 실행시점의 클래스 속성 값으로 객체의 값이 결정된다.

#Method Types
#1. instance method : 데코레이터가 없는 메소드, self로 시작하는 변수
#   개별적인 객체를 참조하는 함수
#2. 클래스 메소드
#   @classmethod
#3. staticmethod
#   저장되는 메모리가 다른


#클래스 메소드 #객체가 모드 공유한다.
#클래스 변수를 사용할 때 이용한다.


#static 메소드


#duck typing
#파이썬에서 다형성을 가지는 방법


#magic method(연산자 오버로딩)
#원하는 작동방식으로 구현 가능
#매개변수의 포켓몬을 넣고, 매개변수의 인수를 넣고 싶을 때 함수 오버로딩이 안되기 때문에 어떻게 구현?

#클래스의 간의 연관관계
#Aggregation and Composition
#1. Aggregation

#다중 상속 대체 가능
#aggregation과 composition 구성 강도에 따라서
#self.fly
#wing객체를 만들어서 인수로 전달
#flyclass를 상속하는 fly와 nofly 를 만든다.. overiding으로 처리 #다형성을 이용
#setter를 이용해 class의 fly 속성을 변경해주기


#composition
# class Fly :
#     def fly(self):
#         print("하늘을 난다.")
#
# class Pikachu :
#     #def __init__(self, name, hp, fly):
#     #     self.name = name
#     #     self.hp = hp
#     #     self.fly_behavior = fly
#     # aggregation으로 구현
#
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         self.fly_behavior = Fly() #클래스 내부에서 만들어 준다. (Composition)

#11장 모듈
import myMath
#특정 함수를 파일에 옮기고 import를 이용해 불러온다.

while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input("Input number : "))
        if myMath.isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number!')
    elif menu == '4':
        n1, n2 = map(int, input("Input first second number : ").split())
        n1, n2 = min(n1, n2), max(n1, n2)
        # numbers = input("Input first second number : ").split()
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        # if n1 > n2:
        #     n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if myMath.isprime(number):
                print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break
    else:
        print('Invalid Menu!')

























