import scrapy


class DxSpider(scrapy.Spider):
    name = "dx"
    #爬虫的域，不写就是对爬虫的域不做限制
    allowed_domains = ["baidu.com","douban.com"]
    start_urls = ["https://www.baidu.com/"]

    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'
    }

    def parse(self, response):
        """

        :param response:
        :return:
        """
        title = response.xpath('//title/text()').extract()
        #构造请求对象
        url = 'https://www.douban.com'
        yield scrapy.Request(
            url=url,
            headers=self.headers,
            #回调解析，让该请求对象的响应，指定由那个方法做解析
            #在此处表示，豆瓣的响应由parse_douban_response方法解析响应
            #此处并不需要指定该方法的参数，传参过程在scrapy底层中已经集成
            callback=self.parse_douban_response,
            #防止该请求对象被过滤
            dont_filter=True,
            #函数与函数之间，变量的传递，参数的传递
            #保存图片传递保存路径，获取传递保存图片的名称
            #meta是一个字典，负责函数与函数之间，变量的传递，参数的传递
            #meta={'自定义的key值':title}
            meta={'name':title}
        )

    def parse_douban_response(self, response):
        """
        解析豆瓣的响应
        :param response:豆瓣的响应对象
        :return:
        """
        #获取百度的标题
        baidu_title = response.meta['name']
        title = response.xpath('//title/text()').extract()
        print(title)

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl dx".split(" "))
