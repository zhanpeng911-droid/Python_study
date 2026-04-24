#模拟树形结构，二叉树

class Node:
    def __init__(self, item):
        self.item = item        #节点的内容
        self.lchild = None      #左子树
        self.rchild = None      #右子树


#定义BinaryTree
class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    #往二叉树中添加元素
    def add(self,item):
        #判断根节点是否为空，如果为空，则设置要添加的内容为：根节点即可
        if self.root is None:
            self.root = Node(item)
            return

        #创建队列。用于记录：二叉树中的每个元素
        queue = []
        queue.append(self.root)
        #循环查找，要添加的元素
        while True:
            #找到根节点
            root_node = queue.pop(0)
            #判断左子树是否为空
            if root_node.lchild is None:
                root_node.lchild = Node(item)
                break
            else:
                queue.append(root_node.lchild)

            #判断右子树是否为空
            if root_node.rchild is None:
                root_node.rchild = Node(item)
                break
            else:
                queue.append(root_node.rchild)

    #自定义函数 breadth_travel 遍历二叉树，获取每个元素，广度优先
    def breadth_travel(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        #具体的获取元素动作，只要队列中有元素。我们就一直获取
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item, end=' ')
            #判断当前节点左子树，右子树是否不为空，如果不为空，就添加到队列里
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


    # 自定义函数 preorder_travel 遍历二叉树，获取每个元素，深度优先-前序
    def preorder_travel(self,root):
        if root is None:
            return
        print(root.item, end=' ')          #根
        self.preorder_travel(root.lchild)  #递归获取，左子树
        self.preorder_travel(root.rchild)  #递归获取，右子树

    # 自定义函数 _travel 遍历二叉树，获取每个元素，深度优先-中序
    # 中序遍历：左 → 根 → 右
    def inorder_travel(self, root):
        if root is None:
            return
        self.inorder_travel(root.lchild)  # 左
        print(root.item, end=' ')  # 根
        self.inorder_travel(root.rchild)  # 右

    # 自定义函数 _travel 遍历二叉树，获取每个元素，深度优先-后序
    # 后序遍历：左 → 右 → 根
    def postorder_travel(self, root):
        if root is None:
            return
        self.postorder_travel(root.lchild)  # 左
        self.postorder_travel(root.rchild)  # 右
        print(root.item, end=' ')  # 根



#测试上述功能
def demo1():
    node = Node('张三')
    print(f'{node.item}')
    print(f'{node.lchild}')
    print(f'{node.rchild}')

    #测试链表
    bt = BinaryTree(node)
    print(f'{bt}')

#测试queue队列的pop函数
def demo2():
    queue = []
    queue.append('A')
    queue.append('B')
    queue.append('C')

    print(queue)
    #pop()根据索引删除元素，并返回元素
    print(queue.pop(0))
    print(queue.pop(0))

#测试广度优先 深度优先
def demo3():
    bt = BinaryTree()
    bt.add('0')
    bt.add('1')
    bt.add('2')
    bt.add('3')
    bt.add('4')
    bt.add('5')
    bt.add('6')
    bt.add('7')
    bt.add('8')
    bt.add('9')
    #广度优先遍历
    # bt.breadth_travel()
    bt.preorder_travel(bt.root)
    print('\n')
    bt.inorder_travel(bt.root)
    print('\n')
    bt.postorder_travel(bt.root)



if __name__ == '__main__':
    # demo1()
    # demo2()
    demo3()




