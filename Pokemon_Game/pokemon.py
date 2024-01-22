import random
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
        criti = random.randint(0, 3)
        target.hp -= (self.power + criti)
        print(f'공격력 : {self.power + criti}')