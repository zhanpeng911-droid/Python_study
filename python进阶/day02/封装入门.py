
class Prentice(object):
    # 1.1 初始化属性.
    def __init__(self):
        self.kongfu = '[自研 摊煎饼果子技术]'
        self.__money = 500        # 徒弟的私房钱, 私有化了.

    # 1.2 行为, 摊煎饼.
    def make_cake(self):
        print(f'采用 {self.kongfu} 制作煎饼!')

    # 1.3 定义公共的访问方式(接口), 查看 私房钱.
    def get_money(self):
        return self.__money

    # 1.4 定义公共的访问方式(接口), 修改 私房钱.
    def set_money(self, money):
        self.__money = money


# 2. 定义 徒孙类, 继承子 徒弟类.
class TuSun(Prentice):
    pass

# main方法中测试.
if __name__ == '__main__':
    # 3. 创建 徒孙类对象.
    ts = TuSun()
    # 4. 尝试访问 从父类(徒弟类)中继承过来的内容.
    print(ts.kongfu)
    ts.make_cake()

    # 5. 尝试访问 父类(徒弟类)的私房钱.
    # print(f'(徒孙) 看到了 (徒弟)的私房钱: {ts.money}')
    # print(f'(徒孙) 看到了 (徒弟)的私房钱: {ts.__money}')
    # print(f'(徒孙) 看到了 (徒弟)的私房钱: {ts.get_money()}')

    # 修改 徒弟的私房钱.
    ts.set_money(666666666)

    print(f'(徒孙) 看到了 (徒弟)的私房钱: {ts.get_money()}')











