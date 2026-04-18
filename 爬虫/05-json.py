import json

"""json.dumps:能够将字典类型数据转换成字符串，且中文会有\u5c0f\u660e字符串的转换"""
# dict1 = {'name': '小明','age':20}

#ensure_ascii=False:防止中文被转义
# result1 = json.dumps(dict1,ensure_ascii=False)
# print(result1,type(result1))

"""json.loads:能够将字符串形式下对字典数据转换成字典"""
# result2 = json.loads(result1)
# print(result2,type(result2))

# json.dump和json.load方法操作的对象是文件
"""json.dump: 能够将字典格式的数据写入到文件"""
# with open('1.json', 'w', encoding='utf-8')as f:
#     json.dump(dict1, f, ensure_ascii=False)

"""json.load: 能够从文件中读取数据，且能够还原它的数据类型"""
# with open('1.json', 'r', encoding='utf-8')as f:
#     read_result = json.load(f)
# print(read_result, type(read_result))

"""美化输出"""
dict1 = {'name': '小明','age':20}
print(json.dumps(dict1,indent=4,ensure_ascii=False))

"""sort_keys=True: 根据key值进行排序"""
data = [{'a':'A','c':3.0,'b':(2,4)}]
print('SORT:',json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False))

"""消除空格，紧凑输出：separators=(",",":")"""
data = [{'a':'A','c':3.0,'b':(2,4)}]
print(json.dumps(data,separators=(',',':'),ensure_ascii=False))





