"""
多态介绍:
    概述:
        多态指的是同一个事物在不同场景下表现出来的不同形态, 状态.
        Python中的多态指的是, 同一个函数, 传入不同的对象, 会实现不同的结果.
    多态的前提条件:
        1. 要有继承关系.
        2. 要有方法重写.
        3. 要有父类引用指向子类对象.            an:Animal = Dog()   an:Animal = Cat()      狗是动物, 猫是动物
    好处:
        提高代码的可维护性. 实现: 1个函数, 多种效果.
    应用场景:
        父类型充当函数形参的类型, 这样可以接受其任意的子类对象, 实现: 传入什么(子类)对象, 就调用其对应的功能.

    细节:
        有人说, Python中的多态其实是"伪多态", 因为 函数的形参类型, 并不能严格限制必须传入该类型或者其子类型的对象,
        其实传入其它类型的对象也是可以的.
"""

class Animal(object):
    def speak(self):
        print('动物会叫')

class Dog(Animal):
    def speak(self):
        print('狗汪汪汪')

class Cat(Animal):
    def speak(self):
        print('猫喵喵喵')

def make_noise(an:Animal):
    #接收动物的对象，实现传入什么动物就对应动物的叫声
    an.speak()


if __name__ == '__main__':
    c = Cat()
    d = Dog()

    make_noise(d)














