"""

插入排序介绍:
    概述/原理：
    1. 假设列表的第 1 个元素为：分界值，然后将 所有小于该分界值的数据，都放到分界值的左边。将所有大于或者等于分界值的数据，都放到分界值的右边.
    2. 此时我们得到的列表就是：小，分界值，大 这样的格式，第二轮我们又可以从这个列表中，左右双方再次找出两个分界值，重复上述的步骤，
    3. 我们发现：左右双方可以各自独立相互排序，重复上述的步骤，直至所有的数据全部排列成功.

    比较的轮数        每轮比较的次数        谁 (索引) 和谁 (索引) 比较        外循环 (i)，内循环 (j)
        1                 4                      1 和 0                          1-0
        2                 3                      2 和 0-1                        2-0
        3                 2                      3 和 0-2                        3-0
        4                 1                      4 和 0-3                        4-0
    核心3点:
        1. 比较的轮数.       列表的长度 - 1
        2. 每轮比较次数.     列表长度 - 1 - 轮数   for j in range():
        3. 谁和谁交换.       j索引 和 j+1索引  对应的元素, 比较, 然后决定是否交换.


    时间复杂度
        最优时间复杂度：O(n)
        最差时间复杂度：O(n平方)
"""

def quick_sort(list,start,end):
    if start >= end:
        return
    #定义变量left 和 right 表示起始 和结束索引
    left = start
    right = end
    #定义变量middle(mid)
    mid = list[start]
    #具体排序过程
    while left < right:
        while left < right and list[right] > mid:
            right -= 1
        list[left] = list[right]

        while left < right and list[left] < mid:
            left += 1
        list[right] = list[left]
    list[left] = mid
    quick_sort(list,start,left-1)
    quick_sort(list,right+1,end)



    print(list)




if __name__ == '__main__':
    quick_sort([5,8,1,7,9,4,3,6,2],0,8)




























