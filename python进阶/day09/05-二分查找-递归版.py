"""
二分查找 算法解释：
    概述：
        它是一种高效的查找类的算法，也叫：折半查找.
    前提：
        要查找的列表，必须是：有序的.
    原理：
        找到中间值，如果要查找的值 和 中间值一致，就返回True
        如果比中间值小，就去 中值前 (中间值的左边) 查找.
        如果比中间值大，就去 中值后 (中间值的右边) 查找.
"""

def binary_search(mylist, item):
    """
    递归版，二分查找
    :param mylist: 记录的元素，注意：有序的
    :param item: 要被查找的元素
    :return: 查找的结果
    """
    n = len(mylist)

    #判断列表的长度，如果小于等于0，直接返回False
    if n <= 0:
        return False

    mid = n // 2

    if item == mylist[mid]:
        return True
    if item < mylist[mid]:
        return binary_search(mylist[:mid], item)
    else:
        return binary_search(mylist[mid+1:], item)

    return False


if __name__ == '__main__':
    print(binary_search([1,2,3,4,5,6,7,8,9], 7))






