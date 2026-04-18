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

#继承子类  
class Tusun(Prentice):
    pass

if __name__ == '__main__':
    ts = Tusun()
    ts.make_cake()
    ts.make_master_cake()
    ts.make_school_cake()



















