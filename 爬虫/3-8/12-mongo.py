# import pymongo
#
# mongo_client = pymongo.MongoClient('localhost', 27017)
# mongo_client['db2']['info'].insert_one({'name':"pzw"})

"""
通过python完成增删改查的操作
"""

import pymongo


#先定义类
class MongoData:
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['db2']['table']


    #增
    def add_data(self,data):
        self.db.insert_one(data)

    #查
    def search_data(self,query=None):
        if query is None:
            result = self.db.find({})
        else:
            result = self.db.find(query)

        for item in result:
            print(item)

    #改
    def update_data(self,con,value):
        self.db.update_many(con,value)

    #删
    def delete_data(self,query):
        self.db.delete_many(query)


if __name__ == '__main__':
    mongo = MongoData()
    # mongo.add_data({"name":"张三","age":20})  #通过对象调用方法
    mongo.search_data()

con = {"name":"张三"}
value = {"$set":{"age":26}}
mongo.update_data(con,value)

mongo.delete_data({"age":26})
