import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    #第一种采集方式，将翻页的地址全部放到start_urls列表中
    # start_urls = [f"https://movie.douban.com/top250?start={25*i}&filter=" for i in range(10)]

    def start_requests(self):
        """
        重写scrapy底层，第一个请求的发送方法
        类继承，继承父类，重写父类方法
        :return:
        """
        #for循环翻页
        for page in range(10):
            #拼接完整地址
            url = f"https://movie.douban.com/top250?start={25 * page}&filter="
            #构建请求对象
            yield scrapy.Request(
                url=url,
                #底层该方法中构建请求对象
                # callback=self.parse,
                # dont_filter=True,
            )


    def parse(self, response):
        movie_title_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
        for title in movie_title_list:
            item = {
                'title': title,
            }
            yield item








if __name__ == '__main__':
    from scrapy import cmdline
    # cmdline.execute("scrapy crawl douban".split(" "))
    #忽略日志输出
    cmdline.execute("scrapy crawl douban --nolog".split(" "))
