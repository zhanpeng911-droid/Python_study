class Prentice(object):
    def __init__(self):
        self.kongfu = '[自研煎饼果子技术]'
        self.__money = 500

    def __make_cake(self):
        print(f'采用{self.kongfu}摊煎饼')

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money


    #提供公共函数，用于访问摊煎饼这个私有方法
    def make(self):
        self.__make_cake()


class TuSun(Prentice):
    pass

if __name__ == '__main__':
    ts = TuSun()
    print(ts.kongfu)
    print(f'徒弟的私房钱为：{ts.get_money()}')

    ts.make()
















