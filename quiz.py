import random

user_random_min = int(input("最小數: "))
user_random_max = int(input("最大數: "))

num = random.randint(user_random_min, user_random_max)
count = 0
while True:
    num_guess = int(input("輸入一個數字: "))
    count = count +1
    print ("猜了", count, "次")
    if num_guess > num: 
        print("比答案大")
    elif num_guess < num:
        print("比答案小")
    else:
        print("猜對了")
        break