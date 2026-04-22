#创建 singleLinkedList
from singlenode import SingleNode


class SingleLinkedList(object):
    def __init__(self,node = None):
        self.head = node

    # is_empty(self) 链表是否为空
    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return True if self.head == None else False

    # length(self) 链表长度
    def length(self):
        #定义变量 count = 0
        count = 0
        cur = self.head
        #循环实现获取每个节点即可，只要cur不为none，就说明还有节点
        while cur is not None:
            #走这里说明有节点，计数器加一，然后设置cur为当前节点的下个节点
            count += 1
            cur = cur.next
        return count



    # travel(self. ) 遍历整个链表
    def travel(self):
        #定义变量 count = 0
        count = 0
        cur = self.head
        #循环实现获取每个节点即可，只要cur不为none，就说明还有节点
        while cur is not None:
            print(cur.item)
            #重新设置cur为当前节点的下个节点
            cur = cur.next

    # add(self, item) 链表头部添加元素
    def add(self,item):
        #把item封装成节点
        new_node = SingleNode(item)
        #设置新节点，指向之前旧的头结点
        new_node.next = self.head
        #设置新节点为新的头节点
        self.head = new_node


    # append(self, item) 链表尾部添加元素
    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    # insert(self, pos, item) 指定位置添加元素
    def insert(self,pos,item):
        """
        往指定位置，添加元素
        :param index:
        :param item:
        :return:
        """
        if pos <= 0:
            self.add(item)

        if pos >= self.length():
            self.append(item)

        else:
            #定义变量count 用于表示：插入位置前的那个元素的索引
            count = 0
            cur = self.head

        while count < pos-1:
            count += 1
            cur = cur.next
        new_node = SingleNode(item)
        new_node.next = cur.next

        cur.next = new_node


    # remove(self, item) 删除节点
    def remove(self,item):
        cur = self.head

        prev = None
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next


            else:
                prev = cur
                cur = cur.next





    # search(self, item) 查找节点是否存在























