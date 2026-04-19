"""
案例：回顾open语法，引出with open 写法，上下文管理器

"""

# file_obj = open('test.txt', 'w', encoding='utf-8')
#
# file_obj.write('好好学习，天天向上')
#
# file_obj.close()


# try:
#     file_obj = open('test.txt', 'r', encoding='utf-8')
#     file_obj.write('好好学习，天天向上')
#     file_obj.close()
# except:
#     print('程序出问题了')
# finally:
#     file_obj.close()
#     print('资源释放了')

with open('test.txt', 'w', encoding='utf-8') as file_obj:

    file_obj.write('好好学习，天天向上')
    #释放资源，不需要写了，代码执行完毕后，会自动释放
    # file_obj.close()




