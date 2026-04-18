import pymongo

class MongoDB(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['db2']['test']

    def add_many_data(self,data):
        self.db.insert_many(data)


    def gaoji_data(self):
        """
        语法：链接对象。aggregate([{}])
        相同的年龄去归类 $取这个字段的值
        1.分组
        2.计算年龄总和
        3.数据不直观，统计人数

        :return:
        """
        # result = self.db.aggregate([
        #     {"$group":{
        #         "_id":"$age",
        #         "sum_age":{"$sum":"$age"},
        #         "count":{"$sum":1}
        #     }}
        # ])
        # """根据性别进行分组"""
        # result = self.db.aggregate([
        #     {'group':{
        #         "_id":"$gender",
        #         "count":{"$sum":1},
        #         "average":{"$avg":"age"},
        #         "name": {"$push":"$name"}
        #     }}
        # ])


        '''$match:查询 统计年龄大于二十
        1.匹配年龄大于20岁个人信息
        2.针对的是你匹配的数据进行分组，得到分组的结果
        3.针对你分组的结果是否显示哪一个
        '''
        # result = self.db.aggregate([
        #     {'$match': {"age": {"$gt": 20}}},
        #     {'$group': {"_id": "$gender", "count": {"$sum": 1}}},
        #     {"$project": {"_id": 0,"count": 1}}
        # ])

        '''sort:排序'''
        result = self.db.aggregate([{"$sort":{"age":1}}])

        '''limit:显示前三条数据'''
        result = self.db.aggregate([{"$sort":{'skip':3},{'$limit':2}}])

        for item in result:
            print(item)


if __name__ == '__main__':
    db = MongoDB()
    data = [
        {"name": "陈明", "age": 35, "gender": "男", "province": "上海市"},
        {"name": "周晓慧", "age": 26, "gender": "女", "province": "浙江省"},
        {"name": "吴强", "age": 41, "gender": "男", "province": "四川省"},
        {"name": "郑雪", "age": 24, "gender": "女", "province": "黑龙江省"},
        {"name": "赵建国", "age": 50, "gender": "男", "province": "陕西省"},
        {"name": "孙静", "age": 31, "gender": "女", "province": "福建省"},
        {"name": "李伟华", "age": 45, "gender": "男", "province": "山东省"},
        {"name": "王婷", "age": 22, "gender": "女", "province": "湖北省"},
        {"name": "刘洋", "age": 38, "gender": "男", "province": "广东省"},
        {"name": "杨思雨", "age": 26, "gender": "女", "province": "云南省"}
    ]
    # db.add_many_data(data)
    #查询
    db.gaoji_data()





















