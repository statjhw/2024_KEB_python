import random
import sys
import time
from pokemon import *
from pokemon_other import *
def attack_info(target) :
    if target.hp > 0 :
        print(f"{target.name}의 남은 피 :{target.hp}")
    else :
        print(f"{target.name}의 남은 피 : 0")




p1 = Pikachu('피카츄',random.randint(45,55),random.randint(1,3) ,'전기', 1)

k1 = Kubok('꼬북이',random.randint(45,55),random.randint(1,3) , '물', 1)

c1 = Charmander('파이리',random.randint(45,55),random.randint(1,3) , '불', 1)

p1 = Pebbles('꼬마돌',random.randint(45,55),random.randint(1,3) , '돌', 2)

d1 = Dialga("디아루가",random.randint(100,130),random.randint(1,3) , '전설', 5)

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

