from python进阶.day08.singleLinkedList import SingleLinkedList
from singlenode import SingleNode

class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

#3.在main方法中调试
if __name__ == '__main__':
    sn1 = SingleNode('张三')
    # sn2 = SingleNode(20)
    # sn1.next = sn2      #设置：sn1节点的下一个节点为sn2

    print(sn1.item)     # 10
    print(sn1.next)     # <__main__.SingleNode object at 0x000001E70592F750>



    # 创建链表类对象
    ll = SingleLinkedList(sn1)
    print(f'链表对象{ll}')
    print(f'头结点：{ll.head}')

    #判断列表是否为空
    print(ll.is_empty())

    #打印列表长度
    print(f'列表长度：{ll.length()}')
    print('-'*20)

    #往列表的头部添加元素
    ll.add('李四')
    ll.add('王五')

    #中间插入
    ll.insert(-0,'张三')

    #删除元素
    ll.remove('王五')

    #遍历链表
    ll.travel()







