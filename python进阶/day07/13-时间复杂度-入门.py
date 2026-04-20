"""
数据结构 和 算法介绍：
    概述/目的：
        1. 掌握好数据结构 和 算法，可以大大提升程序的性能.
        2. 面试的高频考点.
        3. 程序 = 数据结构 + 算法
    名词解释：
        数据结构：存储 和 组织数据的方式，例如：栈，堆，队列，数组，链表，树...
        算法：为了解决实际业务问题，而想出来的 办法 或者 思路.
"""
import time
#案例1 穷举法
#需求：已知a+b+c = 1000,且 a ** 2 + b ** 2 = c ** 2,请问a,b,c的解决方式有哪些
#思路一穷举法

# start = time.time()
#
# for a in range(1,1001):
#     for b in range(1,1001):
#         for c in range(1,1001):
#             if a+b+c==1000 and a ** 2 + b ** 2 == c ** 2:
#                 print(a,b,c)
#
# end = time.time()
# print(end-start)

#思路2：代入法

start = time.time()

for a in range(1,1001):
    for b in range(1,1001):
        c = 1000 - a - b

        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)

end = time.time()
print(end-start)




















