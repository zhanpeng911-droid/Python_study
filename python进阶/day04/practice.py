"""
定义一个闭包，用于求解方程的y与x值的变化，例如 y = ax + b。

"""

# def outer(a, b):
#     def inner(x):
#         return a * x + b
#     return inner
#
# if __name__ == '__main__':
#     f = outer(1, 2)
#     print(f(1))

# def func_count():
#     num1 = 0
#     def func1():
#         nonlocal num1
#         print('hello,world')
#         num1 += 1
#         print(f'执行了{num1}次')
#     return func1
#
# if __name__ == '__main__':
#     f = func_count()
#     f()
#     f()
#     f()

"""
（3）请使用装饰器方式来统计输出100000句"黑马程序员YYDS"的执行时间。
"""
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'执行时间{end-start}s')
#         return result
#     return wrapper
#
#
# @timer
# def print_info():
#     for i in range(10000):
#         print('yyds')
#
#
# if __name__ == '__main__':
#
#     print_info()


"""
（4）定义一个函数, 返回字符串, 使用装饰器实现对这个字符串添加后缀.txt。
"""

def add_txt(func):
    def inner():
        result = func()
        return result + ".txt"
    return inner

@add_txt
def num():
    return "hello"

if __name__ == '__main__':
    print(num())

"""
通用装饰器 通常都写 *args, **kwargs ，因为：

1. 适配任何函数 - 不管原函数有没有参数、有多少参数
2. 避免报错 - 如果原函数有参数但你没写，会报 TypeError
"""










