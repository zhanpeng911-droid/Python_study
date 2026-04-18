import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#继承的是CrawlSpider类
class ImgSpider(CrawlSpider):
    name = "img"
    allowed_domains = ["adoutu.com"]
    start_urls = ["https://www.adoutu.com/picture/list/1"]

    rules = (Rule(LinkExtractor(restrict_xpaths=r'//nav[@class="flex items-center justify-center gap-1 py-6"]/a[1]'), callback="parse_item", follow=True),)
    #注意：在LinkExtractor提取器对象中，只能接受标签对象，不能接受地址字符串
    #因为在底层中，已经实现了从标签对象中提取地址字符串
    """
    reles:规则对象，元组类型，可以存在多个规则
    LinkExtractor:链接提取器对象
    allow=r"Items/"：链接提取器对象定义的规则
    callback="parse_item"：链接提取器提取地址的响应对象由那个方法做解析
    follow=True：该链接提取器在 链接提取器的地址响应中，是否继续应用链接提取器
    """

    def parse_item(self, response):
        #输出请求的地址
        print(response.request.url)

        href_list = response.xpath('//img/@src').extract()
        title_list = response.xpath('//title/text()').extract()
        for img_url,img_title in zip(href_list, title_list):
            #img_url 表情包地址
            #img_title 表情包标题
            yield scrapy.Request(
                url=img_url,
                callback=self.parse_response_data,
                meta={'title': img_title,'img_url': img_url[-5:]}
            )

    def parse_response_data(self, response):
        """
        解析表情包的二进制数据
        :param response:
        :return:
        """
        #提取表情包的二进制数据
        data = response.body
        #获取html的源码内容，方法是
        #response.body.decode()
        #response.text
        #提取表情包的标题
        img_title = response.meta['title']
        #提取表情包的格式
        img_type = response.meta['img_type']
        """构造数据item的对象"""
        item = {
            'data': data,
            'title': img_title,
            'img_type': img_type,
        }
        yield item


if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl img --nolog".split(' '))

