class student(object):
    def __init__(self):
        self.current_weight = 100 #单位kg

    #跑一次减少0.5kg
    def run(self):
        self.current_weight -= 0.5
        print(f'当前体重为{self.current_weight}')

    #吃一次体重增加2kg
    def eat(self):
        self.current_weight += 2
        print(f'当前体重为{self.current_weight}')



if __name__ == '__main__':
    #创建对象

    #测试跑步的功能
    xm = student()
    xm.run()
    xm.eat()








