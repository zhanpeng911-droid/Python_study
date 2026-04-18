"""
使用装饰器的时候，要注意：
    装饰器的内部函数 格式要和原函数保持一致，要么都是无参无返回，要么都是无参有返回，要么都是有参无返回，要么有参有返回
"""

#需求：定义无参无返回值的原函数get_sum，用于计算两个整数和，在不改变该函数的基础上，给这个函数添加友好提示

#内部函数结构 = 原函数（要装饰的函数）结构
def print_info(fn_name):
    def inner():
        print('友好提示，正在努力计算中')
        fn_name()
    return inner

#要被装饰的函数，无参无返回值
@print_info
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f'求和结果为{sum}')

if __name__ == '__main__':
    get_sum()













