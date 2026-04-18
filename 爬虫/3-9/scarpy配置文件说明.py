

# 知识点
# 1.注意配置说明
# 2.制作爬虫日志


# 一般情况下，scrapy的默认并发请求数是8
# 并发：同时，同一时刻
# 并行：排队，交替


"""管道配置"""
#解开注释，表示使用管道，能够接受数据的保存请求
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "baiduspider.pipelines.BaiduspiderPipeline": 300,
#}

"""下载中间件的配置"""
#解开注释，即可使用下载中间件，拦截请求对象，拦截响应对象
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "baiduspider.middlewares.BaiduspiderDownloaderMiddleware": 543,
#}

"""日志的级别"""
#日志不会记录print信息

#ERROR：错误，记录程序报错信息
#WARNING：警告，记录程序警告信息
#INFO：详情信息
#DEBUG：调试模式








