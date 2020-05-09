#队列

#采用List来容纳Queue的数据项。
#将List首端作为队列尾端，将List的末端作为队列首端
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


