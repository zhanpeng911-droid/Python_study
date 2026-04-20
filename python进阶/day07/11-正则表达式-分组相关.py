"""
    正则表达式的规则：
        |           表示：或者的意思
        ()
        \num

        扩展：
            (?P<分组名>)   设置分组
            (?P=分组名)    使用指定的分组

"""
import re

#需求1：列表中有一些水果，喜欢吃：apple 和 pear ，请用正则验证，下述的水果，哪些是喜欢吃的，哪些是不喜欢吃
fruits = ['apple','banana','orange','pear']

#遍历获取每一种水果
for fruit in fruits:
    if re.match('apple|pear',fruit):
        #进这里说明是喜欢吃的水果
        print(f'喜欢吃{fruit}')

    else:
        print(f'不喜欢吃{fruit}')


#需求2：匹配出163，126.qq邮箱
#邮箱规则： 4-20位数字，字母，下划线，

email = '38602166@qq.com'
result = re.match('^[0-9a-zA-Z]{4,16}@(163|126|qq)\\.(com|cn)',email)

if result is not None:
    print(result.group())
else:
    print('未匹配到')

#三元写法
print(f'匹配到：{result.group()}'if result else '未匹配到')




















