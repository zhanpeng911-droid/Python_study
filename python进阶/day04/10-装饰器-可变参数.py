"""
使用装饰器的时候，要注意：
    装饰器的内部函数 格式要和原函数保持一致，要么都是无参无返回，要么都是无参有返回，要么都是有参无返回，要么有参有返回
"""

#需求：定义可变参数的原函数get_sum，用于计算两个整数和，在不改变该函数的基础上，给这个函数添加友好提示

#内部函数结构 = 原函数（可变参数）结构
def print_info(fn_name):
    def inner(*args,**kwargs):
        print('友好提示，正在努力计算中')
        sum = fn_name(*args,**kwargs)
        return sum
    return inner

#要被装饰的函数，无参有返回值
@print_info
def get_sum(*args,**kwargs):

    sum = 0
    #求所有位置参数的和，即：*args -》元组
    for i in args:
        sum += i

    #求所有关键字参数的和，即 **kwargs -》字典
    for i in kwargs.values():
        sum += i
    return sum

if __name__ == '__main__':
    print(get_sum(1,2,3,a=4,b=5,c=6))
