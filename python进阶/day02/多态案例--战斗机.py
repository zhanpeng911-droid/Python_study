"""
需求:
    构建对象对战平台object_play
        1 英雄一代战机（战斗力60）与敌军战机（战斗力70）对抗。英雄1代战机失败！
        2 卧薪尝胆，英雄二代战机（战斗力80）出场！，战胜敌军战机！
        3 对象对战平台object_play, 代码不发生变化的情况下, 完成多次战斗.

分析:
    抽象战机类 HeroFighter  AdvHeroFighter；敌机EnemyFighter;
    构建对象战斗平台, 使用多态实现

"""

class HeroFighter(object):
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter(object):
    def power(self):
        return 70

def object_play(hf,ef):
    if hf.power() >= ef.power():
        print('英雄机胜利')

    else:
        print('敌机胜利')




if __name__ == '__main__':
    hf = HeroFighter()
    hf2 = AdvHeroFighter()
    ef = EnemyFighter()

    object_play(hf,ef)
    object_play(hf2, ef)
















