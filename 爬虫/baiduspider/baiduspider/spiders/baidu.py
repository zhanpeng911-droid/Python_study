import scrapy


class BaiduSpider(scrapy.Spider):
    #爬虫的名称
    name = "baidu"
    #规定，爬虫程序的域，可以做更改
    allowed_domains = ["baidu.com"]
    #爬虫请求起始的地址，可以做更改
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        """
        注意点：对列表中地址的请求对象的构建，集成到了底层中
        用来解析start_url列表地址的响应
        :param response: 列表中地址的响应对象
        :return:
        """
        #直接对response使用xpath语法，返回的结果是一个selector对象列表
        title = response.xpath("//title/text()")
        #我们需要从对象列表中，提取数据需要使用的提取器
        #extract()：提取列表所有的对象的data内容
        #extract_first（）：提取列表中第一个selector对象的data内容
        #               若没有提取到会产生报错
        title_result = title.extract()
        print(title_result)

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl baidu".split(" "))




















