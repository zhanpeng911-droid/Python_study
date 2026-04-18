"""
需求：
    定义一个地瓜类
"""

class SweetPoster(object):
    def __init__(self):
        self.cook_time = 0  #烘烤的时间
        self.cook_state = '生的' #地瓜状态
        self.condiments = [] #添加的调料

    def cook(self,time):
        if time < 0:
            print('传入烘烤时间非法，请校验后重新传入')
        else:
            self.cook_time += time

            if 0 <= self.cook_time <= 3:
                self.cook_state = '生的'
            elif 3 <= self.cook_time <= 7:
                self.cook_state ='半生不熟的'
            elif 7 <= self.cook_time <= 12:
                self.cook_state = '熟了'
            else:
                self.cook_state = '已烤焦，糊了'

    #添加调料
    def add_condiments(self,condiments):
        self.condiments.append(condiments)


    def __str__(self):
        return f'烘烤时间:{self.cook_time},烘烤状态:{self.cook_state}，调料:{self.condiments}'



if __name__ == '__main__':
    digua = SweetPoster()
    digua.cook(2)
    digua.cook(7)

    digua.add_condiments("酱油")
    digua.add_condiments("辣椒")

    print(digua)




