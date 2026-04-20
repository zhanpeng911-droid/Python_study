"""
正则规则：
    # .                任意的1个字符，除了\n
    # \.               取消。的特殊用法，就是1个普通的.
    # a                代表1个字符a
    # [abc]            代表：a,b,c中任意的1个字符
    # [^abc]           代表：除了a,b,c以外的任意1个字符
    #
    # [0-9]            代表：任意的1个整数，例如：0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # \d               代表：任意的1个整数，效果同上.   \d = [0-9]
    # \D               代表：除了整数外的任意1个字符，即：\D = [^0-9]
    # \s               代表：空白字符，例如：空格，tab键等...
    # \S               代表：非空白字符.
    # \w               代表：非特殊字符，例如：字母，数字，下划线(_)，汉字
    # \W               代表：特殊字符.
"""

import re

# .                任意的1个字符，除了\n
result = re.match('it.','ita')
result = re.match('it.','it\n')

# \.               取消。的特殊用法，就是1个普通的.
result = re.match('hm\.','hm.')

# [abc]            代表：a,b,c中任意的1个字符
result = re.match('[abc]hm','ahm')

# [^abc]           代表：除了a,b,c以外的任意1个字符
result = re.match('[^abc]hm','xhm')

# [0-9]            代表：任意的1个整数，例如：0, 1, 2, 3, 4, 5, 6, 7, 8, 9
result = re.match('[0-9]hm','2hm')

# \d               代表：任意的1个整数，效果同上.   \d = [0-9]
result = re.match('\dhm','2hm')
result = re.match('\dhm','ahm')

# \D               代表：除了整数外的任意1个字符，即：\D = [^0-9]
result = re.match('\Dhm','2hm')

# \s               代表：空白字符，例如：空格，tab键等...
result = re.match('\shm','\nhm')

# \S               代表：非空白字符.
result = re.match('\Shm','2hm')

# \w               代表：非特殊字符，例如：字母，数字，下划线(_)，汉字
result = re.match('\whm','2hm')

# \W               代表：特殊字符.
result = re.match('\Whm','#hm')





if result is not None:
    print(result.group())
else:
    print('未匹配到')

#三元写法
print(f'匹配到：{result.group()}'if result else '未匹配到')








