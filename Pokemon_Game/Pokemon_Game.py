import random
import sys
import time
def attack_info(target) :
    print(f"{target.name}의 남은 피 :{target.hp}")
random.randint(45,55)
class Pokemon :

    def __init__(self, input_name, input_hp, input_level, input_type, input_tier):
        self.__name = input_name
        self.__hp = input_hp
        self.__level = input_level
        self.__type2 = input_type
        self.__tier = input_tier
        self.power = 5 * self.level + self.tier * 5
    @property
    def name(self) -> str:
        '''
        name_getter : 포켓몬의 이름을 반환하는 함수
        :return: str
        '''
        return self.__name
    @name.setter
    def name(self, input_name) :
        '''
        name_setter : 포켓몬의 이름을 설정하는 함수
        :param input_name: 변경하고 싶은 이름
        :return: void
        '''
        self.__name = input_name

    @property
    def hp(self) :
        return self.__hp

    @hp.setter
    def hp(self, input_hp) :
        self.__hp = input_hp

    @property
    def level(self) :
        return self.__level

    @level.setter
    def level(self, input_level) :
        return self.__level

    @property
    def type2(self):
        return self.__type2

    @property
    def tier(self):
        return self.__tier

    def info(self) :   #각 포켓몬 class의 오버로딩 또는 데코레이터할 예정

        print('포켓몬 정보'.center(14))
        print('-'*14)
        print(f'{self.name}'.center(14))
        print('type :', self.type2.rjust(6))
        print('hp :', str(self.hp).rjust(9))
        print('공격력 :', str(self.power).rjust(7))
        print('level :', str(self.level).rjust(6))
        print('tier :', str(self.__tier).rjust(7))

    def attack(self, target) :
        target.hp -= self.power
        print(f'공격력 : {self.power}')

class Pikachu(Pokemon) :
    def attack(self,target) :
        super().attack(target)
        print(f'피카피카!!! {self.name}이(가) {target.name}을(를) {self.type2} 공격합니다. 찌릿')

class Kubok(Pikachu) :
    def attack(self,target):
        super().attack(target)
        print(f'꼬북꼬북!!! {self.name}이(가) {target.name}을(를) {self.type2} 공격합니다. 물대포!!!')

class Charmander(Pokemon) :
    def attack(self,target) :
        super().attack(target)
        print(f'파이파이!!! {self.name}이(가) {target.name}을(를) {self.type2} 공격합니다. 파이어!!')

class Pebbles(Pokemon) :
    def attack(self,target) :
        super().attack(target)
        print(f'꼬마꼬마!!! {self.name}이(가) {target.name}을(를) {self.type2} 공격합니다. 원펀치!!')

class Dialga(Pokemon) :
    def attack(self, target):
        super().attack(target)
        print(f'{self.name}이(가) {target.name}을(를) {self.type2} 공격합니다. 드루와!!')
random_hp = random.randint(45,55)
random_level = random.randint(1,3)
p1 = Pikachu('피카츄',random_hp,random_level, '전기', 1)
random_hp = random.randint(45,55)
random_level = random.randint(1,3)
k1 = Kubok('꼬북이', random_hp, random_level, '물', 1)
random_hp = random.randint(45,55)
random_level = random.randint(1,3)
c1 = Charmander('파이리', random_hp, random_level, '불', 1)
random_hp = random.randint(45,55)
random_level = random.randint(1,3)
p1 = Pebbles('꼬마돌',random_hp, random_level, '돌', 2)
random_hp = random.randint(100,105)
random_level = random.randint(1,3)
d1 = Dialga("디아루가",random_hp, random_level , '전설', 5)

target_lst = [p1, k1, c1, p1]


print('포켓몬 월드에 오신 것을 환영합니다. \n당신의 포켓몬을 선택해 주세요.')

while True :
    try :
        choice = input('1) 피카츄   2) 꼬북이   3)파이리   4)게임 종료 ')
        random_hp = random.randint(45, 55)
        random_level = random.randint(1, 3)
        if choice == '1' :
            your_Pokemon = Pikachu('피카츄', random_hp, random_level, '전기', 1)
            break
        elif choice == '2' :
            your_Pokemon = Kubok('꼬북이',random_hp, random_level, '물', 1)
            break
        elif choice == '3' :
            your_Pokemon = Charmander('파이리',random_hp, random_level, '불', 1)
            break
        elif choice == '4' :
            sys.exit('게임 종료')
        else :
            raise Exception
    except Exception as err:
        print('다시 입력하세요 !')
print("당신의 포켓몬이 정해졌습니다!!!")
your_Pokemon.info()

time.sleep(2)

while True :
    choice = input("미지의 포켓몬이 나타났습니다. 1)결투 2)회피 ")
    if choice == '1' :
        target = random.choice(target_lst)
        print("결투가 시작합니다.")
        time.sleep(1)
        print("상대 포켓몬 정보")
        target.info()
        print()
        random = 0
        time.sleep(4)
        while True :
            if random == 0 :
                time.sleep(3)
                print("공격입니다.")
                your_Pokemon.attack(target)
                time.sleep(3)
                print('상대', end = ' ')
                attack_info(target)
                time.sleep(4)
                print()
                if target.hp <= 0 :
                    time.sleep(2)
                    print("승리 !!!")
                    break
                random = 1
            elif random == 1 :
                time.sleep(3)
                print("공격 당합니다..")
                target.attack(your_Pokemon)
                time.sleep(3)
                print('내 포캣몬', end = ' ')
                attack_info(your_Pokemon)
                time.sleep(4)
                print()
                if your_Pokemon.hp <= 0 :
                    time.sleep(1)
                    print("패배...")
                    break
                random = 0
        break
    elif choice == '2' :
        print("도망갑니다!!!!!")

