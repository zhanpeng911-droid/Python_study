class AC(object):
    #抽象方法
    #制冷
    def cool_wind(self):
        pass

    #制热
    def hot_wind(self):
        pass

    #左右摆风
    def swing_l_r(self):
        pass

class Media(AC):
    #抽象方法
    #制冷
    def cool_wind(self):
        print('美的空调 核心制冷技术 制作冷风')

    #制热
    def hot_wind(self):
        print('美的空调 核心制热技术 制作热风')


    #左右摆风
    def swing_l_r(self):
        print('美的空调 遥控器设置 左右摆风')

class Gree(AC):
    #抽象方法
    #制冷
    def cool_wind(self):
        print('格力空调 核心制冷技术 制作冷风')

    #制热
    def hot_wind(self):
        print('格力空调 太阳能技术 制作热风')


    #左右摆风
    def swing_l_r(self):
        print('格力空调 ai设置 左右摆风')




if __name__ == '__main__':
    #测试美的空调
    m = Media()
    m.cool_wind()
    m.hot_wind()
    m.swing_l_r()

    #测试格力空调
    g = Gree()
    g.cool_wind()
    g.hot_wind()
    g.swing_l_r()













