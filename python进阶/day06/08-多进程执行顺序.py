"""
案例：演示多线程执行顺序.

多线程执行顺序：
    多线程执行具有随机性，原因是因为：CPU在做着高效的切换，即：线程在抢CPU资源，谁抢到，谁执行.
扩展：资源调度策略
    均分时间片：每个线程获取到的CPU的时间都是 几乎一致.
    抢占式调度：谁抢到，谁执行.
        更好的，充分的利用CPU资源，例如：Java，Python用到的都是这个策略.
"""

import threading,time

def print_info():
    time.sleep(0.2)
    #获取当前正在执行的线程对象
    th = threading.current_thread()
    #打印当前的线程对象
    print(f'当前正在执行的线程是：{th}')


if __name__ == '__main__':
    #通过for循环，创建十个线程
    for i in range(10):
        th = threading.Thread(target=print_info)
        #启动线程
        th.start()















