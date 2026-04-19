"""
案例：演示 默认情况下，主线程会等待子进程结束再结束.

    方式：
        1.通过 创建线程的时候，daemon属性实现
        2.通过 线程对象名.setDaemon函数实现

"""

#需求：创建一个子进程，执行完大概需要2秒，而主进程执行完需要1秒，实现该需求，观察结果

import threading,time

def worker():
    for i in range(10):
        print(f'第{i}天上班')
        time.sleep(0.2)

if __name__ == '__main__':
    #创建子进程,守护线程
    # t1 = threading.Thread(target=worker,daemon=True)
    #方式二：通过setDaemon实现
    t1 = threading.Thread(target=worker)
    t1.setDaemon(True)
    #启动子进程
    t1.start()
    #休眠一秒,表示主程序执行需要1秒
    time.sleep(1)
    #打印：主进程执行结束
    print('main进程（主进程）结束')























