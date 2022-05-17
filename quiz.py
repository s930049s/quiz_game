import random
num = random.randint(1, 100)

while True:
    num_guess = int(input("輸入一個數字: "))
    if num_guess > num: 
        print("比答案大")
    elif num_guess < num:
        print("比答案小")
    else:
        print("猜對了")
        break