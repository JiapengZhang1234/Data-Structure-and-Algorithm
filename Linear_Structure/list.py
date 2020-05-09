#创建节点Node
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setDate(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#链表的第一个和最后一个节点最重要
#如果想要访问链表中的所有节点，就必须从第一个节点开始沿着链表遍历下去
#必须要有对第一个节点的引用信息。
#设立一个属性head，保存对第一个节点的引用。空表的head为None

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    #添加元素
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    #从链表头head开始遍历到表尾同时用变量累加经过的节点个数
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    #从链表头head开始遍历到表尾，同时判断当前节点的数据项是不是目标
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
