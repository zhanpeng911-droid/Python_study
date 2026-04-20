"""
正则规则，如下都是 和 数量词 相关：
    ?              数量词，代表：前边的内容出现 0次 或者 1次
    *              数量词，代表：前边的内容出现 0 ~ n
    +              数量词，代表：前边的内容出现 1 ~ n
    {n}            数量词，恰好n次
    {n,}
    {n,m}
"""
import re

#演示正则表达式，校验多个字符
#\d? 即：要么一个任意整数，要么没有
result = re.match('\d?it','2it')

#验证  *
result = re.match('\d*it','12432it')
result = re.match('\d*it','it')

#验证  +
result = re.match('\d+it','12432it')
result = re.match('\d+it','it')

# {n}            数量词，恰好n次
result = re.match('\d{3}it','234it')
result = re.match('\d{3}it','34it')

# {n,}          至少n次
result = re.match('\d{3,}it','23465it')


# {n,m}
result = re.match('\d{3,7}it','2344543it')







if result is not None:
    print(result.group())
else:
    print('未匹配到')

#三元写法
print(f'匹配到：{result.group()}'if result else '未匹配到')



















