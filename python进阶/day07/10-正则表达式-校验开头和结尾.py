"""
正则表达式的规则：
    ^  代表正则的开头
    $  代表正则的结尾

"""

import re

# ^  代表正则的开头
result = re.match('\dit','2it')             #Y
result = re.match('^\dit','a1it')           #N
# $  代表正则的结尾
#需求：必须以xyz任意一个字符或者任意一个数字结尾
result = re.match('it[xyz0-9]','it1')
result = re.match('it[xyz0-9]$','itxabc')

#扩展：校验手机号   规则：1.长度必须是11位  2.第二位数字必须是3，4，5，6，7，8，9，  3.第1位数字必须是1  4.必须是纯数字
result = re.match('^1[3-9]\d{9}$','13123456789')         #Y
result = re.match('^1[3-9]\d{9}$','131234567890')        #N
result = re.match('^1[3-9]\d{9}$','1312345678a')         #N
result = re.match('^1[3-9]\d{9}$','13123456789')         #N




if result is not None:
    print(result.group())
else:
    print('未匹配到')

#三元写法
print(f'匹配到：{result.group()}'if result else '未匹配到')










