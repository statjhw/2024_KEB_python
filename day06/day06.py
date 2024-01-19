#과제
#1
# def good() -> list :
#     '''
#     chapter 9 things to do
#     :return: list
#     '''
#
#     harry_porter = input().split()
#     return harry_porter
#
# print(good())

#2
# def get_odd(n) :
#     '''
#     1부터 n까지의 홀수를 발생시키는 제네레이터
#     :param n: int
#     :return: int
#     '''
#     for i in range(1, n+1, 2) :
#         yield i
#
# cnt = 0
# odds = get_odd(9)
# for odd in odds :
#     cnt += 1
#     if cnt == 3 :
#         print(f'Third number is {odd}')
#         break

#3
# def test(func) :
#     '''
#     데코레이터 함수, 함수 시작하면 strat 출력, 함수 끝나면 end 출력
#     :param func: function
#     :return: closure function
#     '''
#     def test_in(*args, **kwargs) :
#         print('start')
#         result = func(*args, **kwargs)  #이줄에서 함수가 호출된다.
#         print('end')
#         return result
#     return test_in
#
# # @test
# def greeting() :
#     print("안녕하세요~")
#
#
# t = test(greeting)
# t()

#namespace
#함수 내부의 변수를 찾고 없으면 밖에서 찾는다.
#global 키워드를 이용한 지역변수를 전역변수로 바뀌는 법
#_, __

#재귀함수
#factorial함수 for문 이용해 구현
#def factorial_reoetition(n) -> int :
#     '''
#     반복문을 이용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: 팩토리얼 값, int
#     '''
#     result = 1
#     for i in range(2, n+1) :
#         result = result * i
#     return result
#
# # print(factorial_reoetition(int(input())))
#
# def factorial_recursion(n) :
#     '''
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: function, int
#     '''
#     if n == 1 :
#         return 1
#     else :
#         return n * factorial_recursion(n-1)
#
# number = int(input())
# print(factorial_reoetition(number))
# print(factorial_recursion(number))
#반복문을 이용한 구현이 더 빠르다.

#비동기 함수
#예외 처리

import random

# numbers = list()
# for i in range(10) :
#     numbers.append(random.randint(1, 100))
# print(numbers)


# numbers = [random.randint(1, 100) for _ in range(10)]
# print(numbers)
# try :
#     pick = int(input(f'Input index (0~{len(numbers)-1}) : '))
#     print(numbers[pick])
# except :
#     print("Out if range : Wrong index number")
#모든 예외를 받는다.


# numbers = [random.randint(1, 100) for _ in range(10)]
# print(numbers)
# try :
#     pick = int(input(f'Input index (0~{len(numbers)-1}) : '))
#     print(numbers[pick])
#     print(5/0)
# except IndexError as err:
#      print(f"Wrong index number\n{err}")
# except ValueError as err:
#     print(f"Input Only Number~\n{err}")
# except ZeroDivisionError as err:
#     print(f"The denominator cannot be 0.\n{err}")
# except Exception :
#     print("Error occurs")

#예외 순서대로 예외를 받는다.
#raise : 예외를

# class OopsException(Exception) :
#     pass
#
#
# numbers = [random.randint(1, 100) for _ in range(10)]
# print(numbers)
# try :
#     pick = int(input(f'Input index (0~{len(numbers)-1}) : '))
#     print(numbers[pick])
#     print(5/2)
#     raise OopsException("Oops~~") #exception! #c++의 throw와 같다.
# except IndexError as err:
#      print(f"Wrong index number\n{err}")
# except ValueError as err:
#     print(f"Input Only Number~\n{err}")
# except ZeroDivisionError as err:
#     print(f"The denominator cannot be 0.\n{err}")
# except OopsException as err :
#     print(f"Oops {err}")
# except Exception as err :
#     print("Error occurs")
# else :
#     print(f"Error occurs : {err}")



#데코레이터
# def desc(f) :
#      def wrapper() :
#         print('study')
#         r = f()
#         return r #없을 대
#      return wrapper
#
# def something() :
#     print("do something")
#
# s = desc(something)


#객체
# class Pokemon :
#     def __init__(self, name):   #self -> this와 같은 역할
#         print(f"{name} 포켓몬스터 생성")
#
#
# pikachu = Pokemon('pakchu')
# squirtle = Pokemon('squirtle')

##Attributes
# print(pikachu)      #객체의 메모리 주소를 출력한다.
#
#
# pikachu.nemesis = squirtle
# print(pikachu.nemesis)
# print(squirtle)

#Methods
#객체안에 들어있는 함수

#initialization
#self 실행시점의 객체의 메모리 주소를 가진 변수 c++에서 this와 같은 역할을 한다.
#매개변수와 필드 구분하기
# class Pokemon :
#     def __init__(self, name):   #self -> this와 같은 역할
#         self.name = name
#         print(f"{self.name} 포켓몬스터 생성")
#
#     def attack(self, target):
#         print(f"{self.name}가 {target.name}을 공격합니다.")
#
#
# pikachu = Pokemon('pakchu')
# squirtle = Pokemon('squirtle')
#
#
# print(pikachu.name)
# pikachu.attack(squirtle)


#__init__은 다른 언어의 생성자와는 다르다.
#python __init__, __new__(생성자의 역할)


#클래스 간의 관계
#상속 : is a
#연관 관계 : has a
#의존 관계 : use a

#부모 객체에 들어갈 자리에 자식 객체가 들어갈 수 있다.



# class Pokemon :
#     def __init__(self, name):   #self -> this와 같은 역할
#         self.name = name
#         print(f"{self.name} 포켓몬스터 생성")
#
#     def attack(self, target):
#         print(f"{self.name}가 {target.name}을 공격합니다.")
#
#
# class Pikachu(Pokemon) : #is-a
#     pass

# p1 = Pikachu("피카츄")
# print(p1.name)
#
# #issubclass 함수
# isinstance(Pikachu, Pokemon)

#Override 자식 클래스에서 재정의
#
# class Pokemon :
#     def __init__(self, name):   #self -> this와 같은 역할
#         self.name = name
#         print(f"{self.name} 포켓몬스터 생성")
#
#     def attack(self, target):
#         print(f"{self.name}가 {target.name}을 공격합니다.")
#
#
# class Pikachu(Pokemon) : #is-a
#     def attack(self, target):
#         print(f"{self.name}이 {target.name}을 일렉트릭 공격!")
#     def ekectric_info(self) :
#         print("전기 계열의 공격을 합니다.")


# class Squirtle(Pokemon) :
#     pass
#
# p1 = Pikachu('피캬츄')
# s1 = Squirtle('꼬북이')
# print(p1.attack(s1))
# print(s1.attack(p1))

#super
class Pokemon :
    def __init__(self, name):   #self -> this와 같은 역할
        self.name = name
        print(f"{self.name} 포켓몬스터 생성")

    def attack(self, target):
        print(f"{self.name}가 {target.name}을 공격합니다.")


class Pikachu(Pokemon) : #is-a
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def attack(self, target):
        print(f"{self.name}이 {target.name}을 {self.type} 공격!") #함수 오버라이딩
    def ekectric_info(self) :
        print("전기 계열의 공격을 합니다.")
class Squirtle(Pokemon) :
    pass

p1 = Pikachu('피카츄', '전기')
s1 = Squirtle("피카츄")
p1.attack(s1)
print(p1.name, p1.type)

#다중상속 : 2개 이상의 부모클래스가 있다.
#파이썬의 다중 상속 시 함수의 상속 시 앞 순서에서 상속받은 클래스의 함수를 사용한다. -> 오류가 나지 ㅏㅇㄴㅎ는다.
class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'
class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'
class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

m1 = Mule()
print(m1.says())
print(Mule.__mro__) #상속 순서를 나타낸다.


























