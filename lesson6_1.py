#建立自訂的功能

#function名稱是sayHello
def sayHello(): #沒有參數的function
    print("Hello!")

def sayHello_withName(name):  #有一個參數的function
        print(f"Hello {name}!")


if __name__ == "__main__":
    sayHello_withName("Betty") #引數值傳遞至name參數內