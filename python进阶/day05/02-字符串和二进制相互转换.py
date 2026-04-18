"""
格式：
    字符串.encode(encoding='码表名‘)              一般用utf-8
    二进制字符串.decode(encoding='码表名'))

"""

s1 = '你好'


bytes1 = s1.encode(encoding='UTF-8')
bytes2 = s1.encode(encoding='gbk')
bytes3 = s1.encode()


print(bytes1)
print(bytes2)
print(bytes3)
print('-'*20)

s2 = 'abc12!@#'
bytes4 = s2.encode(encoding='UTF-8')
bytes5 = s2.encode(encoding='gbk')

print(bytes4)
print(bytes5)
print(type(bytes4))
print(type(bytes5))

print(type(b'abc12@#$'))


bs1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'
bs2 = b'\xc4\xe3\xba\xc3'
bs3 = b'abc12!@#'

ss1 = bs1.decode(encoding='UTF-8')
ss2 = bs2.decode(encoding='gbk')
ss3 = bs3.decode(encoding='gbk')

print(ss1)
print(ss2)
print(ss3)