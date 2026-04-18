"""
管理系统文件
主要完成：学生管理系统的 主要业务逻辑的
"""
import time


from student import Student

class studentcms(object):
    #初始化属性，student_list = [学生对象，学生对象...]
    def __init__(self):
        s1 = Student('张三','男','20','131','善良')
        s2 = Student('李四', '男', '42', '189', '好人')
        s3 = Student('王五', '女', '26', '153', '脾气差')
        self.student_list = [s1, s2, s3]

    #定义函数 show_view()用于展示提示界面
    #\t是占位符
    def show_view(self):
        print('*' * 20)
        print('欢迎来的学生管理系统界面')
        print('\t1.添加学员')
        print('\t2.修改学员')
        print('\t3.删除学员')
        print('\t4.查询某个学员')
        print('\t5.显示所有学员')
        print('\t6.保存信息')
        print('\t0.退出系统')
        print('*' * 20)

    #添加学员
    def add_student(self):
        #录入学生信息
        name = input('请录入要添加的学生的姓名：')
        gender = input('请录入要添加的学生的性别：')
        age = int(input('请录入要添加的学生的年龄：'))
        mobile = input('请录入要添加的学生的手机号：')
        des = input('请录入要添加的学生的描述信息：')
        #封装成学生对象
        stu = Student(name, gender, age, mobile, des)
        #把封装好的学生对象，添加到学生列表中
        self.student_list.append(stu)
        #打印提示信息即可
        print(f'添加{name}信息成功')

    #修改学员
    def update_student(self):
        #提示用户录入要修改的学生的姓名
        updata_name = input('请录入要修改学生的姓名：')
        #遍历学生列表，提取每个学生的信息
        for stu in self.student_list:
            #判断当前学生姓名 是否和要修改的学生姓名一致
            if stu.name == updata_name:
                #如果一致就重新录入信息
                stu.gender = input('请录入要修改的学生的性别：')
                stu.age = int(input('请录入修改的学生的年龄：'))
                stu.mobile = input('请录入要修改的学生的手机号：')
                stu.des = input('请录入要修改的学生的描述信息：')
                #核心细节：记得break
                print('修改信息成功\n')
                break
            #如果循环结束，还没有匹配到，就提示查无此人
            else:
                print('查无此人，请校验后重新输入\n')

    #删除学员
    def del_student(self):
        # 提示用户录入要删除的学生的姓名
        del_name = input('请录入要删除学生的姓名：')
        # 遍历学生列表，提取每个学生的信息
        for stu in self.student_list:
            # 判断当前学生姓名 是否和要删除的学生姓名一致
            if stu.name == del_name:
                # 如果一致就删除录入信息
                self.student_list.remove(stu)
                print('删除信息成功\n')
                # 核心细节：记得break
                break
            # 如果循环结束，还没有匹配到，就提示查无此人
            else:
                print('查无此人，请校验后重新输入\n')

    #查询某个学员
    def search_one_student(self):
        # 提示用户录入要查询的学生的姓名
        search_name = input('请录入要查询学生的姓名：')
        # 遍历学生列表，提取每个学生的信息
        for stu in self.student_list:
            # 判断当前学生姓名 是否和要查询的学生姓名一致
            if stu.name == search_name:
                # 如果一致就删除录入信息
                print(stu,end='\n\n')
                # 核心细节：记得break
                break
            # 如果循环结束，还没有匹配到，就提示查无此人
            else:
                print('查无此人，请校验后重新输入\n')

    # 显示所有学员
    def search_all_student(self):
        #判断是否有学生信息
        if len(self.student_list) > 0:
            for stu in self.student_list:
                print(stu)
        else:
            print('暂无学生信息，请添加学生信息')

    #保存信息
    def save_student(self):
        #把列表存储在学生对象， 转成 列表存储字典的形式
        # student_dict = [stu.__dict__ for stu in self.student_list]
        # print(student_dict)
        student_data = str([stu.__dict__ for stu in self.student_list])
        #存进文件夹中
        with open('student.txt', 'w', encoding='utf-8') as f:
            f.write(student_data)

            print('学生信息保存成功！\n')



    #加载学生信息
    def load_student(self):
        try:
            with open('student.txt', 'r', encoding='utf-8') as f:
                student_data = f.read()
                if len(student_data) <= 0:
                    student_data = "[]"

                # 用 eval 把字符串转回列表
                data_list = eval(student_data)

                # 从字典创建学生对象
                self.student_list = [
                    Student(
                        stu_dict['name'],
                        stu_dict['gender'],
                        stu_dict['age'],
                        stu_dict['mobile'],
                        stu_dict['des']
                    )
                    for stu_dict in data_list
                ]
        except FileNotFoundError:
            self.student_list = []

    #程序的入口，在这里完成具体的逻辑
    def start(self):
        while True:
            time.sleep(1)

            self.show_view()
            #输入编号
            input_num = input('请输入您要操作的编号:')
            #根据用户输入的编号，进行对应的操作
            if input_num == '1':
                # print('添加学生\n')
                self.add_student()
            elif input_num == '2':
                # print('修改学生\n')
                self.update_student()
            elif input_num == '3':
                # print('删除学生\n')
                self.del_student()
            elif input_num == '4':
                # print('查询某个学生\n')
                self.search_one_student()
            elif input_num == '5':
                # print('显示所有学生\n')
                self.search_all_student()
            elif input_num == '6':
                # print('保存信息\n')
                self.save_student()
            elif input_num == '0':
                #退出系统需要二次确认
                result = input('您确定要退出吗？(Y/N):')
                #强制转换Y
                if result.upper() == 'Y':
                    print('退出系统\n')
                    break



            else :
                print('输入无效字符，请重新输入\n')




#测试代码
if __name__ == '__main__':
    s_cms = studentcms()
    # s_cms.show_view()
    s_cms.start()











