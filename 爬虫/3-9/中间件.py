"""中间件"""


#下载中间件
#可以自定义类名
#方法名称需要用固定的

# 对应的函数方法
# process_request：拦截所有的请求对象
# process_response：拦截所有的响应对象
# process_exception：拦截异常

# 上述函数方法的返回值
# process_request返回值
# 1. return None
# 不写return也是返回None值
# 该request请求对象传递给下载器或者经过其他类的拦截请求的下载中间件

# 2.return request
# 直接将requests请求对象传递给下载器，不会经过其他的拦截请求的下载中间件

# 3.return response
# 着是和selenium结合使用的，后续在实际使用过程中给大家讲解

# process_response返回值
# 1.return request
# 将该响应的请求对象重新交给调度器，进入下一次请求队列，传递给下载器发送请求(重构请求
# 那么在此处既然做了return request 对应的response会被抛弃掉
# 此时response也不会在经过其他的拦截响应的中间件

# 2.return response
# 将响应传递给其他拦截响应的中间件，最后直接交给引擎，由引擎传递给spider做解析

#京东









