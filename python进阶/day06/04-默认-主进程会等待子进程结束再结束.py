"""
案例：演示 默认情况下，主进程会等待子进程结束再结束.

目的：
    引出下个知识点，如何实现，让主进程结束的时候，它的子进程也同步结束.
"""

#需求：创建一个子进程，执行完大概需要2秒，而主进程执行完需要1秒，实现该需求，观察结果

import multiprocessing,time

def worker():
    for i in range(10):
        print(f'第{i}天上班')
        time.sleep(0.2)

if __name__ == '__main__':
    #创建子进程
    p1 = multiprocessing.Process(target=worker)
    #启动子进程
    p1.start()
    #休眠一秒,表示主程序执行需要1秒
    time.sleep(1)
    #打印：主进程执行结束
    print('main进程（主进程）结束')















