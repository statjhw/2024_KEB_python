# a = 4
# print(a)
#
# #fstring, formating
# base_number = 2
# exp_number = 5
# print(f"밑 {base_number}, 지수 {exp_number}")
# print("밑 {}, 지수 {}".format(base_number, exp_number))
#
# #c like
# print('밑은 %d, 지수는 %d' % (base_number, exp_number))
# #side effect
# #진수
# print(base_number)

#화씨 섭씨 변환

fah = float(input("input fahrenheit : "))
print(f"섭씨 : {(fah - 32) * (5./9.):.4f}") #ftream에서 소숫점 맞추기

print(int('1A', 16))


#git log 특정 commit으로 이동 log에서 오른쪽 reSet~누르고 Hard선택

menu = int(input("1. f->c 2. c -> f : "))
if menu == 1 :
    f = float(input("input F : "))
    print(f"섭씨 : {(f - 32) * (5/9):.4f}")
else :
    c = float(input("input C : "))
    print(f"화씨 : {c * (9/5) + 32 : .4f}")
# \ 줄바꿈 if _ in _