# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class DoubanspiderPipeline:
    def process_item(self, item, spider):
        """

        process_item是scrapy管道的底层方法，不要任意更改
        :param item:数据对象item
        :param spider:
        :return:
        """
        with open('1.txt', 'a+', encoding='utf-8') as f:
            f.write(f"电影名称：{item['title']}\n")
        print(f"数据：{item['title']}保存完成！")
        return item


class MongoDBPipeline:
    #将数据保存到数据库中

    def open_spider(self, spider):
        """
        第一次执行管道，启动该方法，每次运行项目，该方法都只会运行一次
        :param spider:
        :return:
        """
        #创建链接对象
        self.mango = MongoClient('localhost', 27017)
        #创建连接数据库与集合
        self.db = self.mango['douban']['data']


    def process_item(self, item, spider):
        """

        process_item是scrapy管道的底层方法，不要任意更改
        :param item:数据对象item
        :param spider:
        :return:
        """
        #将数据插入到数据库中
        self.db.insert_one(item)
        print(f"数据：{item['title']}插入完成！")

    def close_spider(self, spider):
        """
        爬虫结束前，启动该方法，每次运行项目，该方法都只会运行一次
        :param spider:
        :return:
        """
        self.mango.close()
