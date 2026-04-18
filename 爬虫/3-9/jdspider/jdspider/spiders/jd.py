import scrapy


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = ["https://book.jd.com/booksort.html"]

    def parse(self, response):
        #提取分类的名称
        cat_name_list = response.xpath('=//*[@id="booksort"]/div[2]/dl/dd[1]/em/a/text()').extract()
        #提取分类的地址
        cat_url_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dd[1]/em/a/@href').extract()
        print(cat_name_list,len(cat_name_list))
        print(cat_url_list,len(cat_url_list))

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl jd".split(' '))