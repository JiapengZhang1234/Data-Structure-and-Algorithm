#使用顺序查找的方式来查看列表中是否存在某个元素
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

#testlist1 = [1,2,32,8,17,19,42,13,0]


#print(sequentialSearch(testlist1,3))
#print(sequentialSearch(testlist1,13))


#如果列表中的元素是按照大小排好顺序的有序表
#其比对过程与普通的列表相同
#不同之处在于，如果数据项不存在，比对可以提前结束

def orderSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist2 = [0,1,2,8,13,17,19,32,42]
print(orderSequentialSearch(testlist2,3))
print(orderSequentialSearch(testlist2,13))
