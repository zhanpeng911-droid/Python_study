"""
学员文件
自定义学生类，描述学生信息的,属性：姓名，年龄，联系方式，描述信息
"""
class Student(object):
    def __init__(self, name, gender,age ,mobile,des):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile = mobile
        self.des = des

    def __str__(self):
        return f'姓名:{self.name},性别:{self.gender},年龄:{self.age},联系方式:{self.mobile},描述信息:{self.des}'



if __name__ == '__main__':
    s = Student(name='张三', gender='男', age='20', mobile='111111', des='勇敢')
    print(s)


















