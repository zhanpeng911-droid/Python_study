"""
正则表达式 介绍：
    概述：
        全名叫：Regular Expression，就是 正确的 符合特定规则的 字符串，就叫：正则表达式.
    作用：
        可以用来校验，匹配，过滤指定的数据.
    使用步骤：
        1. 导包.
           import re
        2. 正则校验.
           result = re.match(pattern=正则规则，str=要校验的字符串，flag=0)
           参1：正则表达式，参2：要校验的字符串，参3：可选项，例如：忽略大小写，多行模式等...
        3. 获取到匹配的数据.
           result.group()
    正则表达式 涉及到的函数：
        1. 用于做校验的，替换的.
           match()
           search()
           compile().sub()
        2. 用于 获取值的.
           group()

    细节：
    1. 正则表达式不独属于Python语言，市场上你见过的绝大多数的语言都支持正则，例如：Python，PHP，Java，Go，JavaScript..  且规则都是一样的.
    2. 我们学正则表达式，主要学习的是：正则表达式的规则，因为正则表达式已经存在很多年了，你的需求 (校验邮箱，手机号，身份证号)，网上一搜一大堆.
    3. 关于正则，要求大家：能看懂别人写的式子，且会基于需求简单的修改即可.
正则表达式 常用规则：
    [abc]
    [^abc]
    a
    \d          代表一个整数
    \D          除了整数外任意一个字符
    \s
    \S
    \w
    \W

    ^
    $
    ?
    *
    +
    {n}
    {n,m}

    |
    ()
    \num

"""

import re

#案例1，正则表达式匹配字符
#正则表达式：.it的意思是：第一个字符任意写，后续两个字符必须是it
# print(re.match('.it','ait'))        #能匹配，返回的是：正则对象
# print(re.match('.it','aait'))       #不能匹配，返回的是：none
# print(re.match('.it','aitb'))       #不能匹配，返回的是：正则对象

#案例2：校验字符是否是ait，bit，cit，hit，git
# result = re.match('[abchg]it','git')

#案例3：校验字符串第一个字符不是a,b,c,后两个字符必须是hm
# result = re.match('[^abc]hm','vhm')

#案例4：校验 数字开头，任意多个字符结尾
#[0,9]      代表任意的一个整数
#。*        代表任意个字符
result = re.match(r'[0-9].*','a1mit')        #match是从左往右匹配的，跳不了
# result = re.search('[0-9].*','a1mit')        #search是从左往右，开始匹配的，从任意字符开始，只要匹配即可



# result = re.match(pattern='.it', string='1it')

if result is not None:
    print(result.group())
else:
    print('未匹配到')


















