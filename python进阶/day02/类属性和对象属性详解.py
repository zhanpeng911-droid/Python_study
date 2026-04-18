from tkinter.font import names


class Student(object):

    #老师名字
    teacher_name = '刘老师'

    def __init__(self):
        self.name = '张三'


if __name__ == '__main__':
    #创建学生类对象
    s1 = Student()
    s2 = Student()

    print(f's1对象的 对象属性：{s1.name}')
    print(f's2对象的 对象属性：{s2.name}')

    #修改s1对象的属性值
    s1.name = '王五'

    print(f's1对象的 对象属性：{s1.name}')
    print(f's2对象的 对象属性：{s2.name}')

    print(f's1对象的 对象属性：{s1.teacher_name}')
    print(f's2对象的 对象属性：{s2.teacher_name}')


















