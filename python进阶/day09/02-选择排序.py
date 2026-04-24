"""

选择排序介绍:
    概述/原理：
    每轮比较，都找到最小值所在的索引，然后和 最小索引进行交换即可.
    大白话：选择排序就是把符合条件的元素给选择出来，进行排序.
    推理过程：假设列表长度为 5
    比较的轮数        每轮比较的次数        谁 (索引) 和谁 (索引) 比较        外循环 (i)，内循环 (j)
        0                 4                      0 和 1-4
        1                 3                      1 和 2-4
        2                 2                      2 和 3-4
        3                 1                      3 和 4
    核心3点:
        1. 比较的轮数.       列表的长度 - 1
        2. 每轮比较次数.     列表长度 - 1 - 轮数   for j in range():
        3. 谁和谁交换.       j索引 和 j+1索引  对应的元素, 比较, 然后决定是否交换.


    时间复杂度
        最优时间复杂度：O(n)
        最差时间复杂度：O(n平方)
"""

def select_sort(list):
    for i in range(0, len(list)-1):       #比较的轮数----提醒：循环要从0开始，
        min_index = i
        for j in range(i+1, len(list)):   #每轮比较次数
            if list[min_index] > list[j]:
                min_index = j
        #看min_index值有无发生变化，有变化就是找到最小值了，进行交换
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]

    print(list)




if __name__ == '__main__':
    select_sort([10,9,8,7,6,5,4,3,2])




























