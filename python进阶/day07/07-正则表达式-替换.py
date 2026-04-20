"""
正则表达式 替换，介绍：
    涉及到的函数：
        import re
        re.compile(正则表达式1).sub(用来替换的字符串2，要操作的字符串3)  #把3中能和1匹配的内容，用2来替换

    上述格式的语法糖
         re.sub(正则表达式1,用来替换的字符串2，要操作的字符串3)

"""
import re
#案例1：演示 正则替换
s1 = '车主说，你的刹车片该换了啊，嘿嘿，桀桀桀'

rg = r'啊|嘿|桀'

#开始具体的替换动作
#分解版
# rg_obj = re.compile(rg)             #获取正则对象
# result = rg_obj.sub('1',s1)    #实现正则替换
# print(result)

#合并版
result = re.compile(rg).sub('1',s1)

print(result)

#案例2：正则替换的语法糖，re.sub(正则表达式1,用来替换的字符串2，要操作的字符串3)

s2 = '车主说，你的刹车片该换了啊，嘿嘿，桀桀桀'

result2 = re.sub(rg,'2',s2)

print(result2)

s3 = '车主说，你的刹车片该换了啊，嘿嘿，桀桀桀'
result3 = s3.replace('嘿嘿','1')      #不支持正则
print(result3)


