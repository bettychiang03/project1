#一個專案內的主執行的py檔,必須要使用__name__的判斷式
'''
這是一個猜數字遊戲
是1到100的範圍
'''

import random

min = 1
max = 100
count = 0
random_value = random.randint(min,max)
print(random_value)

if __name__ == "__main__":
    print("這是專案內,被python執行的主要執行檔")
    print("=============猜數字遊戲=================")
    while True:
        count += 1
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        if keyin >= min and keyin <= max :
            if(keyin == random_value):
                print(f"猜對了,答案是:{random_value}")
                print(f"您總共猜{count}次")
                break
            elif keyin > random_value:
                print("再小一點")
                max = keyin - 1
            elif keyin < random_value:
                print("再大一點")
                min = keyin + 1
            print(f"您已經猜了{count}次")
        else:
            print("超出範圍")
    print("遊戲結束")

print(keyin)