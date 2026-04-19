import threading

#定义函数，模拟：写代码
def coding():
    for i in range(10):
        print('正在敲代码')

#定义函数，模拟：听音乐
def music():
    for i in range(10):
        print('正在听音乐')

if __name__ == '__main__':
    #创建线程对象
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    #启动线程
    t1.start()
    t2.start()

    pass


























