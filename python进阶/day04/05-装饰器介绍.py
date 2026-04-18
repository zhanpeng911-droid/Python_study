"""
    闭包函数的一种写法
    前提条件：
        1.有嵌套
        2.有引用
        3.有额外功能
        4.有返回
"""

#发表评论前先登录

def check_login(fn_name):
    def inner():
        print('登录中。。登录成功')
        fn_name()
    return inner

@check_login
def comment():
    print('发表评论')

if __name__ == '__main__':
    # comment()

    # pp = check_login(comment)    #加了括号是调用，不加括号就是对象
    # pp()

    #在定义函数的时候，加上@装饰器名字，之后就正常调用该原函数即可
    comment()










