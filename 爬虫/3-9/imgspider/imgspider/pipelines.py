# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class ImgspiderPipeline:
    def process_item(self, item, spider):

        os_path = os.getcwd() + '/表情包/'
        if not os.path.exists(os_path):
            os.makedirs(os_path)
        def process_item(self,item, spider):

            #提取表情包的二进制
            data = item['data']
            #提取表情包的标题
            title = item['title']
            #提取表示包的格式
            img_type = item['img_type']
            with open(os_path + title + img_type,'wb') as f:
                f.write(data)
                print(f'表情包{title}-----保存成功')
            return item
