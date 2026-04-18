
def fun1():
    print('hello')

if __name__ == '__main__':
    # print(fun1)

    #f2 = fun1()  输出为none

    # print(fun1()) #输出为none

    f2 = fun1
    print(f2)           #地址
    print(f2())        #None








