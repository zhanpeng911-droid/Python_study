"""
案例：自定义 数据迭代器，即：自定义生成器，从原始文件中读取所有的数据，然后按照指定条数，生成每批次的数据.
目的：为后续的AI模型训练课程做铺垫，后续训练模型的时候，不是一次性喂给大批量的数据，而是分批次来训练的.
"""
import math


# 需求：读取 jaychou_lyrics.txt 文件的数据，按照 n条/批次，生成生成器，并测试.
# 1. 定义 dataset_loader()，接受：每批次的数据条数，获取 生成器.
def data_loader(batch_size):
    """
    自定义的数据迭代器，按照n条批次，获取生成器
    :param batch_size:每批次的数据条数
    :return:生成器对象
    """

    # 获取到所有数据，readlines()一次性读取所有行
    with open('./data/jaychou_lyrics.txt', 'r', encoding='utf-8') as src_f:
        data_lines = src_f.readlines()
    #数据总条数
    line_count = len(data_lines)
    # print(data_lines[:10])
    # print(line_count)

    #数据的总批次数，总批次 = 数据总条数/每批次的数据条数
    batch_count = math.ceil(line_count / batch_size)   #math.ceil(100/8) = 12.5 -> 13

    #遍历批次总数，获取到具体的每个批次编号
    for batch_id in range(batch_count):
        """
            batch_id 就代表着 批次 id，例如：0 代表第 1 批，1 代表第 2 批. 假设每批次 8 条数据.
            batch_id = 0，代表第 1 批，8 条/批次，则第 1 批的数据为：data_lines[0:8]，即：获取索引为 0 ~ 8 的数据，包左不包右
            batch_id = 1，代表第 2 批，8 条/批次，则第 2 批的数据为：data_lines[8:16]，即：获取索引为 0 ~ 8 的数据，包左不包右

        """
        #具体的生成每批次的数据，然后通过yield放到生成器中（并返回生成器）
        yield data_lines[batch_id * batch_size : batch_id * batch_count + batch_size]



if __name__ == '__main__':
    #测试上述的函数，获取指定条数的批次数据
    # my_generator = data_loader(5)

    #获取第一批次的数据
    # print(next(my_generator))

    #获取第二批的数据
    # print(next(my_generator))

    my_generator = data_loader(8)
    for data in my_generator:
        print(data)


    #比这个数字大的所有整数中，最小的那个整数
    # print(math.ceil(10.0))          #ceil()向上取整,天花板数        10
    # print(math.ceil(10.1))          # ceil()向上取整,天花板数       11
    # print(math.ceil(10.5))          # ceil()向上取整,天花板数       11










