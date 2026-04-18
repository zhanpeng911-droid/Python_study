# class Car:
#     def run(self):
#         print("走路")
#
#
# if __name__ == '__main__':
#     c1 = Car()
#     c1.run()

# class Car(object):
#     def run(self):
#         print("我是run函数")
#         print("汽车会跑")
#
#
#     def work(self):
#         print("我是run函数")
#         self.run()
#
#
#
#
#
#
# if __name__ == '__main__':
#     c1 = Car()
#     c2 = Car()
#
#     c1.color = 'Red'
#     c1.num = 4
#
#     print('{c1.color},{c1.num}')

"""魔法方法"""

# class Car:
#     def __init__(self):
#         self.color = 'blue'
#         self.num = 5
#
#
#     def get_sum(self,c,d):
#         a = c
#         b = d
#         return a + b
#
#     #魔法方法str，输出语句打印对象时，会自动调用，一般用于打印对象的各个属性值
#     def __str__(self):
#
#
#
#
#
# if __name__ == '__main__':
#     c1 = Car()          #创建对象自动调用init魔法方法
#     #如下格式就不是定义属性值，而是修改属性值
#     c1.color = 'red'
#     c1.num = 7
#     print(f'{c1.color},{c1.num}')
#
#     c2 = Car()          #创建对象自动调用init魔法方法
#     c2.color = 'blue'
#     c2.num = 5
#     print(f'{c2.color},{c2.num}')
#
#     print(c1.get_sum(10,20))
#     print(c1)

class Car:
    def __init__(self, color,number):
        self.color = color
        self.number = number


    #魔法方法str，输出语句打印对象时，会自动调用，一般用于打印对象的各个属性值
    def __str__(self):
        return f'{self.color},{self.number}'

    #魔法方法del，del删除对象的时候，或者文件执行结束后，自动调用它，用于释放资源
    def __del__(self):
        print(f'{self}')



if __name__ == '__main__':
    c1 = Car('黑色','1')          #创建对象自动调用init魔法方法


    print(f'{c1.color},{c1.number}')

    print(c1)
    print("-"*20)

    del c1
    c2 = Car('lan','4')
    print(c2)




