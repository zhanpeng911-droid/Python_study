"""
细节：
    1.进程之间数据是相互隔离的，不能共享
    2. 子进程相当于是父进程的副本，即：把父进程的内容会拷贝一遍，单独执行。注意：main 外资源.
    3. 案例：定义 1 个列表，1 个进程添加数据，另 1 个进程查看数据，看是否能查到数据即可.

"""

#需求：在不同进程中修改列表 my_list = [],并新增元素，并观察结果
import multiprocessing,time
#表示其共享资源
my_list = []

def writer_data():
    for i in range(1,6):
        #具体的添加数据到列表的动作
        my_list.append(i)

        print(f'add:{i}')

    print(f'write:{my_list}')

def read_data():
    print(f'read:{my_list}')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=writer_data)
    time.sleep(0.2)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p2.start()


















