from pokemon import *
class Pikachu(Pokemon) :
    def attack(self,target) :
        super().attack(target)
        print(f'피카피카!!! {self.name}이(가) {target.name}을(를) {self.type2} 공격합니다. 찌릿')

class Kubok(Pokemon) :
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
