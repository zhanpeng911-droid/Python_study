"""
    1.多个装饰器 装饰一个函数，装饰的顺序是 由内向外的
    2.但是多个装饰器的执行顺序是，由上往下的
"""

#需求：发表评论前，需要先登录用户，再进行验证码验证，在不改变原有函数基础上，对功能做增强

#登录功能
def check_user(fn_name):
    def inner():
        print('登录中')
        fn_name()
    return inner
#校验验证码的功能
def check_code(fn_name):
    def inner():
        print('校验验证码')
        fn_name()
    return inner


#原函数
@check_user
@check_code
def comment():
    print('发表评论！')

if __name__ == '__main__':
    # cc = check_code(comment)
    # comment = check_user(cc)
    # comment()

    comment()

"""
装饰：由内到外
"""


























