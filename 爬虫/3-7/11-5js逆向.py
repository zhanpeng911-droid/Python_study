"""
    1.js逆向的分类
    2.js逆向常见的几种定位方法
    3.js调试
    4.第三方库执行js代码
"""

#js的分类
#请求参数的逆向
#响应数据的逆向

"""请求参数的逆向"""
#js逆向常见的几种定位方法：定位js加密代码位置

#1.通过开发者工具search搜索窗口，输入关键字定位js

#2.通过观察启动器，定位js
#启动器：该请求触发，调用了js文件的哪些方法

#3.通过xhr断电调试，定位js加密代码位置

"""
pip install js2py
pip install PyExecJS
"""

# import js2py
#
# #创建js预加载环境
# js = js2py.EvalJs()
# with open('1.js','r')as f:
#     data = f.read()
# ##将js代码，写入环境中
# #js.execute(data)
# ##通过环境调用js执行方式
# #print(js.parse_sign(''))

# import execjs
#
# #创建js预加载环境
# with open('1.js','r')as f:
#     data = f.read()
# js = execjs.compile(data)
# result = js.call('parse_sign','')
# print(result)











