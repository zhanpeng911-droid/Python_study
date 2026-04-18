import requests
import execjs
import json

# 目标网站:https://fanyi.youdao.com/#/TextTranslate
url = 'https://dict-trans.youdao.com/webtranslate/sse'
# 请求头参数
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
# 载荷参数
with open('1.js', 'r', encoding='utf-8') as f:
    js = f.read()
# 先编译
js_code = execjs.compile(js)
# 调用js函数 数据类型: 字典
data = js_code.call('C', "t2he2k4m2g6QKRigK0KAmSpXKgAezywG")
data['i'] = "world"
data['from'] = "auto"
data['useTerm'] = "false"
data['domain'] = "0"
data['dictResult'] = "true"
data['keyid'] = "webfanyi"
# print(data)
# 发请求,获取响应数据
res = requests.post(url, headers=head, data=data)
# print(res.text)
'''
没有获取到响应数据
    请求头参数携带少了
    加密参数是否有问题
'''
# 读取解密js代码
with open('解密.js', 'r', encoding='utf-8') as f:
    js_1 = f.read()
# 编译
js_code_1 = execjs.compile(js_1)
# 调用
result = js_code_1.call('decrypt_data', res.text)
# print(result, type(result))  #  字符串类型的数据
# 通过键取值----转为字典类型的数据----json 模块
result_dict = json.loads(result)
print(result_dict['translateResult'][0][0]['tgt'])








