#python 2일차 과제

while True :
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")

    if menu == '1' :
        fahrenheit = float(input("input fahrenheit : "))
        print(f"Fahrenheit : {fahrenheit}, Celsius : {(fahrenheit - 32) * (5/9) : .4f}")
    elif menu == '2' :
        celsius = float(input("input celsius : "))
        print(f"Celsius : {celsius}, Fahrenheit : {celsius * (9/5) + 32 : .4f}")

    elif menu == '3' :
        print('quit program')
        break
