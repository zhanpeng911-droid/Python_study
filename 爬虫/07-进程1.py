# from multiprocessing import Process
# import time
# def index():
#     print(8888)
#
# if __name__ == '__main__':
#     #主进程创建的进程都叫子进程
#     #在此处创建的是子进程
#     #创建子进程t1
#     t1 = Process(target=index)
#     #启动子进程
#     t1.start()
#     time.sleep(1)
#     print('主进程输出')


from multiprocessing import Process
import time
def index(num):
    print(f'子进程输出{num}输出：8888')

if __name__ == '__main__':
    #主进程创建的进程都叫子进程
    #在此处创建的是子进程
    #创建子进程t1
    t1 = Process(target=index,args=('t1',))
    #arfs:以元组的形式传参
    t2 = Process(target=index,args=('t2',))
    #kwargs:以字典的形式传参
    t3 = Process(target=index,kwargs={'num':'t3'})
    #启动子进程
    t1.start()
    print('主进程输出')
    t2.start()
    t3.start()







