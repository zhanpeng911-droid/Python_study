# class Father(object):
#     def __init__(self) -> None:
#         self.gender = '男'
#
#     def walk(self):
#         print('饭后走一走，活到99')
#
# class Son(Father):
#     pass
#
#
# if __name__ == '__main__':
#
#     s = Son()
#
#     f = Father()
#     f.walk()

"""单继承"""

# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子技术]'
#
#     def make_cake(self):
#         print(f'采用{self.kongfu}制作煎饼果子')
#
# #定义徒弟类prentice
# class Prentice(Master):
#     pass
#
# if __name__ == '__main__':
#     #创造徒弟类对象
#     p = Prentice()
#
#     print(f'徒弟从师傅继承过来的属性：{p.kongfu}')
#     p.make_cake()

"""
多继承
    1.py中一个类可以继承多个父类，
    2.如果一个类继承了多个父类，则该子类可以拥有所有父类的属性行为   前提：父类的私有成员除外
    3.如果一个类继承了多个父类，且多个父类有同名的属性和行为，优先参考第一个父类的内容，这个是根据mro实现的
    __mro__
    .mro()
    
"""
# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子技术]'
#
#     def make_cake(self):
#         print(f'采用{self.kongfu}制作煎饼果子')
#
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[现代煎饼果子技术]'
#
#     def make_cake(self):
#         print(f'采用{self.kongfu}制作煎饼果子')
#
# #定义徒弟类prentice
# class Prentice(Master,School):
#     pass
#
# if __name__ == '__main__':
#     #创造徒弟类对象
#     p = Prentice()
#
#     print(p.kongfu)
#
#     p.make_cake()
#
#     print(Prentice.mro())

"""
覆盖
"""

# class Master(object):
#     def __init__(self):
#         self.kongfu = '[古法煎饼果子技术]'
#
#     def make_cake(self):
#         print(f'采用{self.kongfu}制作煎饼果子')
#
#
# class School(object):
#     def __init__(self):
#         self.kongfu = '[现代煎饼果子技术]'
#
#     def make_cake(self):
#         print(f'采用{self.kongfu}制作煎饼果子')
#
# #定义徒弟类prentice
# class Prentice(Master,School):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子技术]'
#
#     def make_cake(self):
#         print(f'{self.kongfu}')
#
# if __name__ == '__main__':
#     #创造徒弟类对象
#     p = Prentice()
#
#     print(p.kongfu)
#
#     p.make_cake()
#
#     print(Prentice.mro())

"""
案例: 演示 方法重写后, 子类如何调用父类的 行为(函数)

问题: 重写后, 子类 如何访问 父类的成员?
答案:
    方式1: 父类名.父类方法名(self)            # self本类当前对象的引用.
    方式2: super().父类方法名()

super 关键字介绍:
    概述:
        它代表 本类当前对象 父类的引用.
    简单理解:
        self 代表自己,  super 代表父类.
    细节:
        1. super()只能初始化第1个父类的成员, 所以 super写法 不适用于 多继承, 更适用于 单继承.
        2. 在单继承关系中, 可以把 super().父类方法名(self) 简写成 super().父类方法名()
        3. 多继承关系中, 如果想精准的初始化某个父类的成员, 要通过 父类名.父类方法名(self) 的方式实现.
"""


class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子技术]'

    def make_cake(self):
        print(f'采用{self.kongfu}制作煎饼果子')


class School(object):
    def __init__(self):
        self.kongfu = '[现代煎饼果子技术]'

    def make_cake(self):
        print(f'采用{self.kongfu}制作煎饼果子')

#定义徒弟类prentice
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def  make_cake(self):
        print(f'{self.kongfu}制作煎饼果子')

    #老师傅传过来的配方
    def make_master_cake(self):
        #父类名。父类方法名
        #初始化父类的 属性
        Master.__init__(self)
        Master.make_cake(self)


    #现代传过来的煎饼果子配方
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)



    #从父类继承过来的行为
    def make_old_cake(self):
        super().__init__()
        super().make_cake()



if __name__ == '__main__':
    #创造徒弟类对象
    p = Prentice()

    p.make_cake()

    p.make_master_cake()
    p.make_school_cake()

    p.make_old_cake()

