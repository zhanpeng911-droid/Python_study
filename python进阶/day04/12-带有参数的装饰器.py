"""
带有参数的装饰器，细节：
    1个装饰器的参数，只能有一个
"""

#需求：定义一个技能装饰 减法运算，又能装饰加法运算的装饰器
#定义装饰器
def func(flag):
    def print_info(fn_name):        #这个才是装饰器，一个装饰器只要一个参数
        def inner(a,b):
            if flag == '+':
                print('正在努力计算加法中')
            elif flag == '-':
                print('正在努力计算减法中')
            fn_name(a,b)
        return inner
    return print_info

@func('+')
def add(a, b):
    result = a + b
    print(result)

@func('-')
def sub(a, b):
    result = a - b
    print(result)

if __name__ == '__main__':
    add(1, 2)

    sub(1, 2)













